# Status of rows R1-R9 on 2026-11-07 (IT33 P3)

Non-canonical annex; the table `reopen_searches.tsv` is left as written. Each row is compared with main and with later packages. "Blocked" names the datum that is missing.

| Row | State | Evidence in main | Missing datum / owner |
|---|---|---|---|
| R1 Q230P protein fate | still useful, blocked | INV-13 and WO-03 hold the question and the design | a band or pulse-label signal for the Q230P protein, by two antibodies; wet lab |
| R2 ACK1 inhibition and WWOX in neural or variant context | still useful, blocked | packages ack1_it11 to it13 read the sources; the datum is absent | WWOX protein or half-life after ACK1 inhibition or TNK2 knockdown in neural or variant cells; wet lab |
| R3 Mahajan 2005 and the HCC ACK1 paper | executed | read in IT12-IT13: decisive datum absent from both | none by reading; a new experiment or publication |
| R4 albendazole SPR | still useful, low, blocked | no later work | SPR sensorgram with controls; operator or librarian |
| R5 ITCH activator | blocked | no compound recorded | a small molecule with measured ITCH activation in neural cells |
| R6 suppressor of WWOX deficiency | executed (IT30 RS-R6) | `rs_r6_it30_20261106`: nine modifier observation rows, no genetic suppressor screen; the earlier NO-MATERIAL is not contradicted | a suppressor screen or cross in fly, zebrafish, mouse or organoid |
| R7 RNF138-hnRNPA0-WWOX | still useful, low, blocked | map row RS-R7 | full text, neural relevance, any inhibitor |
| R8 ACK1 loss at genetic level | still useful, blocked | map row RS-R8 | WWOX protein in Tnk2-null tissue held by a group |
| R9 faint G372R and G137V bands | still useful, blocked | map row RS-R9 | two antibodies and IP or MS on the neural line with the knockout floor; data holders |

**The one reopening taken (R2/R8, zero spend).** PubMed on 2026-11-07, `(ACK1 OR TNK2) AND (WWOX OR Wwox)`: 4 records in total (PMIDs 16288044, 19144635, 20432460, 25738261), all earlier than the table and already read; no new source. The reopening condition is not met; the decision it could change (an ACK1-directed lever to raise WWOX protein in a variant-limited context, Track B) stays unsupported. Not searched: preprint servers.

**Radar link.** The plan read twelve tables and dropped this one, older than twelve packages, in every run. The radar now rotates two of the twelve slots through the older tables by ISO week (cap unchanged), and names the tables not read in a run (`scout_daily.py pick_tables`, test in `test_scout_daily.py`).
