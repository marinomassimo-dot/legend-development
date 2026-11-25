# Checkpoint AI, follow-up of 2026-11-25 (after step 2 batch 2, the pre-read checklist, six newly held papers and one correction; resume from AI plus this file; hypothesis level; not medical advice; this file is not edited once hashed)

Checkpoint AI (`CHECKPOINT_SCI_CONTINUATION_20261125_AI.md`, sha256 `1c19f70441e99040feeaf8599f8e1dd48ba77f34eae4f5ad4e021c55341c68d4`, on main) stays valid except where this file says otherwise. Its section 3 (open work) is replaced by section 3 here.

## 1. CORRECTION (dated 2026-11-25, owed to ADV, from IT's blind check and my own recomputation)

Checkpoint AH (section 3 row 5, section 5 lesson 1) and the increment 1 result carried "Table 3 p values of PMID 35222658 (Yadav 2022) do not reproduce". **That is wrong.** The unlabelled row "Low 4 2 3 9" is in the `<tfoot>` of the XML and belongs to the non-intervention group (group totals 26 and 22; Table 2 margins 6/7/13 and 7/4/11): intervention [[4,4,0],[2,3,13]] chi-square 11.69, p 0.0029 (printed 0.003); non-intervention [[4,2,3],[3,2,8]] chi-square 1.746, p 0.4177 (printed 0.42). The Table 3 against Table 2 margin conflict also disappears. Do not repeat the old claim; the dated correction is in `adv276_acquired_reading_sci_20261125/RESULT_ADV276_SCI_20261125.md` (section 1) and the new check is in the pre-read checklist ("table footer rows in XML are not table body rows"). The AH score of its PREREG row 5 stands through 36601084 only.

## 2. State after checkpoint AI

* **Step 2 batch 2 closed and on main** (2583b55f9): `adv276b_lead_receipts_sci_20261125/RESULT_ADV276_STEP2_BATCH2_SCI_20261125.md`; strict 4 of 10, loose 6 of 10; cumulative ADV-276 strict 16 of 37, loose 23 of 37, reversals 0; wording sent to IT; ten receipts FTR-20261125-{40140574,40674686,40925365,41423560,41496652,42011973,42308317,42587153,42928124,43047766}-01.
* **ADV-276 closed by ADV's rotation** (no batch 3 now). Closing item delivered: `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` (on main, f18e2a18b; this follow-up adds one check).
* **Six papers newly held** (acquisition table `ACQUISITION_TABLE_RANKS26_55_SCI_20261125.tsv`; flag-lookup timeouts had been mistaken for failed acquisition): 33363507, 33854788, 34210081, 27845895, 39178853, 27641496 (full JATS XML with body, supplements and figures for some; PMID and title checked in the XML). 16061658 and 25738261 are not in PMC. Three leads (33363507, 33854788, 34210081) are off the operator PDF list; 16061658 stays. **Reading them is the item AFTER ADV-278** (ADV: do not read them in the ADV-278 hour).

## 3. Open work, in order

1. **ADV-278** (`assignments/ADV-278.md`): ONE-PAGE discriminating experiment spec for a protein-level WWOX assay under valproate (readout able to see WWOX, design with measured exposure, HDAC class control, n derived from the held batch spread, PREREG with four outcomes, what makes it uninformative); held material only, about 60 minutes, hypothesis level; one dated line to ADV at closure and say whether a successor window is wanted. Consumers: DL-REPO-003, RP-008, IT. State progress in this file's successor if the window ends first.
2. Read the six newly held papers (item 2 above) with the pre-read checklist, ten per increment, PREREG with a range before opening, blind second reading.
3. IT may reply on the batch 2 wording and the Kv7 lead; ADV reads the checklist.
4. Standing waits and the ADV-223 operator PDF list unchanged (minus three leads).

## 4. Lessons added since AI

1. A flag-lookup timeout is not an acquisition attempt: a "route result" names the route that was tried.
2. A producer's search negative can be false (the abstract was not searched); a brief clause from another source must be labelled.
3. A table footer row in JATS XML is not a body row; test an assignment against group totals before building a finding on it.
4. Batch work on papers already read once narrowly still yields corrections (strict 4 of 10): the unread classes are where they sit (Methods sentence, source-data sheet, supplement).
