# WO-32 literature half (ADV-043): screening rule, written before any record was screened (SCI, 2026-11-18)

Non-canonical working note. Not medical advice; no dose, route or recommendation; reference genotype class only. The query strings and their hit counts (taken at 2026-11-18 about 01:20 UTC, before any title or abstract was read) are in `QUERY_LOG_COUNTS_SCI_20261118.tsv` in this folder. This file is committed before the record lists are downloaded.

## The question
Is there published evidence on the function or expression of a class IIa HDAC (HDAC4, HDAC5, HDAC7, HDAC9) in the oligodendrocyte lineage, myelination or remyelination, and in which system, species and age? The census of the held record (IT, 2026-11-15) counted 278 hits for HDAC9 and 215 for HDAC7 with oligodendrocyte or myelin terms, by full-text-matching query; none was opened. The counts of my queries differ (580 and 368 by full-text-wide matching, with the added synonyms MITR and HDRP for HDAC9), because the index grew and my query strings are not IT's (IT's strings are not recorded in the held note); the difference is stated, not reconciled.

## Tiers (fixed now)
* **Tier 1 (abstract screen, all records):** every record returned by any of B9_titleabs, B7_titleabs, C_classIIa_titleabs, D4_titleabs_both, D5_titleabs_both (the gene or class named in the title or abstract AND a lineage or myelin term anywhere in the title or abstract). HDAC4 and HDAC5 are in Tier 1 because the class limit concerns the class; they are screened but the primary question is HDAC7 and HDAC9 (ADV-043).
* **Tier 2 (title screen, then abstract if a title passes):** records of A9_fulltext_wide and A7_fulltext_wide that are not in Tier 1 (the lineage and gene terms occur somewhere in the full text, not necessarily in the abstract). Titles only, because the abstract of a record whose abstract does not name the gene cannot state a class IIa result; a paper whose class IIa result lives only in a supplementary table or the body is outside what this screen can find, and is named as the unscreened tail.
* **Not screened (named tail):** records not indexed by Europe PMC (theses, conference abstracts, preprints not indexed); records whose class IIa mention occurs only in full text and whose title does not pass the Tier 2 rule; HDAC4 and HDAC5 beyond Tier 1 (no full-text-wide census was run for them).

## Reason codes (a record gets exactly one)
* **R1** the abstract states an expression, loss-of-function, gain-of-function, binding or pharmacology result for a named class IIa member (HDAC4, 5, 7 or 9) in the oligodendrocyte lineage, myelin, or demyelination or remyelination (any species, age, system).
* **R2** a class or panel result: the abstract names an HDAC family, class II or class IIa as a group, or lists the member inside a panel, in the lineage or myelin, without a separate statement about the member.
* **R3** a pan-HDAC or class I/IIb inhibitor result in the lineage with no class IIa statement.
* **R4** neither (the lineage terms and the gene occur in unrelated contexts: other cell types, tumours, disc, vascular or bone disease, glioma only, review of unrelated fields).
* **R5** a review or commentary; kept in the table only when it makes a class IIa statement and cites a primary source, in which case the primary source is sought.
Tier 2 title rule: advance to abstract only if the title names (a) an HDAC, histone deacetylase or class IIa, or (b) epigenetic, chromatin or transcriptional regulation of oligodendrocyte differentiation, myelination or remyelination, or (c) a class IIa partner (MEF2, NCoR/SMRT complex, 14-3-3). Otherwise R4 by title.

## What is opened in full text
Only records coded R1 by me after the delegate's abstract screen, and R2 whose abstract suggests a class IIa result inside the panel (cap of 8 full texts in this task). Lawful free routes only: Europe PMC full-text XML or the PMC article page; plain client, empty User-Agent, no key, no contact parameter; a challenge page ends that route. A receipt is written only on bytes checked (size and first line first).

## Output table and verdict wording
Table columns: paper, system, species, age, what is stated about class IIa activity or expression, readout, independence (same laboratory or lineage of work as another row, or not). One sentence of verdict, with one of the three labels fixed now: **verified bounded null** (every R1 or R2 record screened was read to the depth stated and none reports a class IIa effect or expression in the lineage; the unscreened tail named), **a lead** (at least one R1 record in a mammalian oligodendrocyte-lineage system reports a class IIa effect on differentiation or myelination), or **mixed**. "Not found in these queries" is never worded as absence in the literature. A null cannot be called verified if any R1 record could not be read to the depth its coding needs; that record is listed as blocked.

## Prediction written now (IPOTESI; scored afterwards in nats against a uniform over the three verdict labels)
* P-A: the screen returns a lead (at least one R1 record with a mammalian oligodendrocyte-lineage result on HDAC4 or HDAC5; on HDAC7 or HDAC9 alone: mixed or null). Probabilities for the verdict on HDAC7 and HDAC9 alone: verified bounded null 0.35, lead 0.25, mixed 0.40. For the class as a whole (including HDAC4 and HDAC5): lead 0.60, mixed 0.30, null 0.10.
* P-B: of the Tier 1 records, R1 are at most 10 and R4 are at least 40%.
* P-C: in Tier 2, at most 3 titles advance and none of those changes the verdict.
