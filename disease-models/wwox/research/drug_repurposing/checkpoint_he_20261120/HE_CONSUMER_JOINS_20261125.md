# Held files and consumer joins (ADV-279 defects), HE, 2026-11-25

Hypothesis level; nothing here is medical advice. Requested by ADV (decisions 1 and 2 on the HE report).

## 1 Held files that are not what their name says

`framework/scripts/held_content_check.py`, run by the save step of `find-fulltext`. Over all of `files/` on this
host: 11,322 files seen, 61 unusable (39 bot-challenge pages, 13 empty, 6 error bodies, 2 HTTP error pages,
1 damaged zip), 6 readable images under another image name. No read receipt names any of the 61. Not covered:
a file of the right kind that holds the wrong article.

## 2 Consumer count without its two false joins

`framework/scripts/consumer_count.py` (`--old-rule` reproduces ADV-265's matching). Ledger-wide: 1,272 joins
become 1,237; 440 studies with a consumer become 433. The seven that lose every consumer: 33958783, 36364214,
36572673, 36979157, 37095367, 39850204, 41751597.

Ranking recomputed with the frozen ADV-265 script on today's tree, once as it is and once with the new units and
pattern (669 held partials; 11 change their count):

* Full ranking, old top 60: 36 records change rank, 5 leave (42137291 25 to 92, 42511902 37 to 188, 33958783 39
  to 577, 39850204 40 to 600, 36498839 47 to 63), 5 enter (41066510, 41744777, 24953239, 30755385, 32023956).
* Order readers use (studies with an unread class), old top 60: 5 leave (33958783, 39850204, 36530994,
  37324196, 35883580); of the 55 that stay, the median shift is 3 places and the largest 41.
* Of the seven, four are in that ranking: 33958783, 39850204, 36979157, 41751597.

**What this changes for ADV-265, 269, 276 and 279 (no re-run).** What was read, and what each reading found, does
not change. What changes is the statement of why a paper was picked: ADV-265 ranked 42137291 first of its frozen
six (SCI had already discounted one placeholder collision by hand), and ADV-276 read 36530994, whose count falls
from 2 to 1; none of the ten of ADV-279, and no study named by an ADV-269 or ADV-272 receipt, changes count. A
yield stated "among the most consumed" holds for the order as frozen, not for the corrected one.

## 3 Limit found while checking: uses that no rule sees

The working model cites 42137291 by author and year ("Thomsen 2026"). Neither the old nor the new rule matches
an author-year mention, so the count misses uses as well as it invented them. Not fixed: it needs a decision on
which author-year forms are unambiguous. Portfolio and investigation rows are single long lines, so an
agenda-style mention inside one still counts.

## 4 Minutes

Spent: about 40 minutes of HE time for the report, the two tools, their tests and the recomputation. Saved per
avoided wrong pick: one reading slot, about 12 minutes (ADV-279 budgeted 120 minutes for ten), plus the
amendment that replaces it.
