# PREREG, ADV-282 increment 6: null-note audit, queue ranks 41 to 48 (SCI, 2026-11-26)

Hypothesis level; reference genotype class; nothing is medical advice. Written and hashed before any source of these rows was opened. What I knew before: the queue table (ranks 41 to 48; DR-H02-005's note has been rewritten since the queue was built, today's text is the one used), each row's source label, held file names only, increments 1 to 5 first readings (frozen) and the increment 4 blind reader still running.

## 1. Rows and what each can show

* DR-I01-006 (Stacpoole 2006, PMID 16651305), DR-I01-001, DR-I01-002, DR-I01-004 (Durie 2018, PMID 29913407), DR-I01-014 (Simpson 2006, PMID 16765624): abstract-level rows; abstracts fetched once through NCBI efetch (no e-mail, no key) into `files/fulltext/adv282_abstracts_sci_20261126/`.
* DA-K01-007: computed from the two held GEO TPM tables (GSE158681, GSE158682); the check is whether the Wwox deletion shows in the same tables; the sentence is recomputed by the blind reader from the tables and the series metadata only.
* DR-H02-005 (label of vigabatrin plus a long literature note): the ADV-287 correction of 2026-11-25 was followed by a blind check; it is not read again and is counted as "already blind-checked", outside this increment's denominators.
* DR-P9-010 (memantine label): a label is not a measurement (increment 3 PREREG, section 3): class NOT ASSESSABLE by construction; the sentence is checked only if the label bytes are held (name search 2026-11-26 of `files/`: to be recorded), otherwise it is listed unread.

## 2. Matching rule and verdicts

Section 2 of `PREREG_ADV282_INC4_SCI_20261126.md` and the verdict definitions of `PREREG_ADV282_INC5_SCI_20261126.md`, unchanged.

## 3. Prediction and rejecting observation

Five abstract rows and one computed row; one label row; one row set aside.

* Assessable (class other than NOT ASSESSABLE) of the 7 read: 3, range 1 to 5. Strict 1, range 0 to 3; loose 1, range 0 to 3.
* **MUST CHANGE (first reading and blind reader separately), of 6 to 7 read: 1, range 0 to 3.** Rejecting observation for the whole increments 4 to 6 (blind reader, 23 sentences): 3 or fewer MUST CHANGE in total (the yield falls below the one third of increments 1 to 3 and 281).

## 4. Method

As increments 4 and 5.
