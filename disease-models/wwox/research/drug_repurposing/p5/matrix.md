# Where each row carries a value (V), is UNKNOWN-led (U) or not applicable (n/a)

V says only that the card's cell holds content. V is NOT favourable and U is NOT unfavourable; a V can be a harm, a negative or a limit. Derived mechanically from cells.json by build_p5.py (first word of the cell). Two limits of that mechanism: (1) a U-led cell can carry content after its UNKNOWN (for example the ethosuximide risk cell names a class-level in-vitro signal); (2) for the deep abstentions the `ev.state` V is a pointer to a repository note, not an evidence statement. The tables hold the text.

## RECUPERO_PROFONDO

| Row | kind | endpoint | b.type | ev.state | ev.func | risk | BLOCK-1 | t.access | t.benefit | feasib. |
|---|---|---|---|---|---|---|---|---|---|---|
| P4-A-01 | candidate | V | V | V | V | V | U | U | U | V |
| P4-A-02 | candidate | V | V | V | V | U | U | U | U | V |
| P4-B-01 | candidate | V | V | V | V | V | U | U | U | V |
| P4-C-01 | candidate | V | V | V | V | V | U | U | U | V |
| P4-D-01 | candidate | V | V | V | V | V | V | U | U | V |
| P4-A-03 | abstention | U | U | V | U | U | U | U | U | V |
| P4-A-04 | abstention | U | U | V | U | U | U | U | U | V |
| P4-A-05 | abstention | U | U | V | U | U | U | U | U | V |
| P4-B-02 | abstention | U | U | V | U | U | U | U | U | V |
| P4-C-02 | abstention | U | U | V | U | U | U | U | U | V |
| P4-C-03 | abstention | U | U | V | U | U | U | U | U | V |
| P4-D-02 | abstention | U | U | V | U | U | U | U | U | V |

## BENEFICIO_PRECOCE

| Row | kind | endpoint | b.type | ev.state | ev.func | risk | BLOCK-1 | t.access | t.benefit | feasib. |
|---|---|---|---|---|---|---|---|---|---|---|
| EB-KD-01 | candidate | V | V | V | V | V | U | U | U | V |
| EB-VGB-01 | candidate | V | V | V | V | V | U | U | U | V |
| EB-ETX-01 | candidate | V | V | V | V | U | U | U | U | V |
| EB-GROWTH-AX-01 | abstention | V | V | V | V | n/a | U | n/a | U | V |
| EB-DEV-AX-01 | abstention | V | V | V | V | n/a | U | n/a | U | V |
| EB-PDANCHOR-AX-01 | abstention | U | V | U | V | n/a | U | n/a | n/a | V |
| EB-HORM-AX-01 | abstention | V | V | V | V | U | U | U | U | V |
| EB-CBD-AX-01 | abstention | V | V | V | V | U | U | U | U | V |
| EB-MTOR-AX-01 | abstention | U | V | U | V | V | U | U | U | V |
