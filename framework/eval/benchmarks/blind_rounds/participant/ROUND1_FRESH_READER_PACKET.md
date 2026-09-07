---
artifact: BLIND ROUND 1 — fresh-reader dispatch packet
case_id: BLIND-FR-001
audience: PARTICIPANT
status: PREPARED — not dispatched. A case begins when an assignment names it.
normative: no
---

# `BLIND-FR-001` — dispatch packet

Five fields. There is no benchmark classification here, no difficulty rating, no contamination
note and no explanation of why this case was chosen — not withheld from you as a courtesy, simply
not part of a reading.

> **Nothing here is medical advice.**

---

```
CASE_ID                    BLIND-FR-001

QUESTION                   What does this paper's title assert, and what does the paper's
                           own evidence establish about that assertion?

PARTICIPANT_SURFACE_HASH   d0adbd8a601fb68e2e027d489aa7db4f5500573c5c4fd30ca7d9bc0d05be12af
                           SHA-256 over the sorted "path\0sha256" lines of every regular
                           file in the surface, .git excluded. Verify it before you read.
                           If it does not match, stop and say so.

ALLOWED_FILES              Everything inside your surface directory, and nothing outside it.
                           The packet within it:
                             sources/article.pdf
                             sources/article.xml
                             sources/supplement_01.pdf
                             sources/supplement_02.pptx
                           Renders you produce yourself go in output/renders/ and are declared
                           with their SHA-256. A caption is not a panel.

STOP_CONDITION             Stop when you can state what the title asserts, name the evidence
                           in this paper that bears on it, and say whether that evidence
                           settles it — or record that the published record does not decide,
                           naming the exact object that would. Do not stop earlier because the
                           answer looks obvious, and do not go on to settle anything the
                           question did not ask.
```
