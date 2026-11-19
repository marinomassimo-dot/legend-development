# L supply state checked against the ledger, and the next investment (SCI, 2026-11-19, after ADV-081; hypothesis level; not medical advice; nothing applied)

**Answer first.** The L list ("not held: Aqeilan 2008, Suzuki 2009 full text, the 2005 and 2007 WWOX-ERBB4 reports, Sardi 2006, the clinical series") mixes two different states. Of the six, **three were already read in August 2026 and only their bytes are missing from this checkout** (Aqeilan 2008 and Suzuki 2009 complete, Aqeilan 2005 partial); **two were never held** (Aqeilan 2007 ERBB4, Sardi 2006); **one is not identified** (the clinical series). No lawful machine route found today restores any of them. The operator's supply request therefore narrows to four full texts plus the bytes of three papers already read. Nothing was fetched around a challenge.

## 1. The six, from the receipt ledger and the manifests (checked by me today)
| Paper | PMID | PMC id | Ledger state | Bytes on disk | What is owed |
|---|---|---|---|---|---|
| Aqeilan 2008, JBC (bone, postnatal survival) | 18487609 | PMC2490770 | `complete_fulltext_read` 2026-08-11, `FTR-20260811-18487609-01` (PMC HTML, 67,363 body characters, 8 figures as images) | absent, 0 of 17 declared artefacts | bytes only; a re-read is not owed unless its locators are to be audited |
| Suzuki 2009, Genes Brain Behav (lde/lde rat) | 19500159 | none | `complete_fulltext_read` 2026-08-06, `FTR-20260806-19500159-01` (30 verified locators; HTML and PDF); then `abstract_only` 2026-11-19, `FTR-20261119-19500159-69` (ADV-067) | absent, 0 of 2 | bytes only (the newer abstract-only receipt understates what the ledger holds) |
| Aqeilan 2005, Cancer Res (WWOX and YAP compete for ErbB-4) | 16061658 | none | `retrieved_not_read` (screen refused) then `partial_fulltext_read` under direct operator authorisation, `FTR-20260811-16061658-02` | absent, 0 of 10 | bytes; a complete read is still open |
| Aqeilan 2007, Cancer Res (Wwox and ErbB4, breast cancer) | 17909041 | none | `abstract_only` 2026-11-08, `FTR-20261108-17909041-99`, bytes not saved | never held | full text |
| Sardi 2006, Cell (presenilin-dependent ErbB4 signalling, astrogenesis) | 17018285 | none | no receipt | never held | full text (it is the paper R3's P1 rests on, now abstract level only) |
| WWOX clinical series | not identified in any record I read | | | | name the paper first (ADV, decision page item 14) |

## 2. Routes tried today (all lawful, none circumvented)
* **Local bytes by SHA-256** (`evidence_presence.py --search` over the uploads cache, Downloads, Documents, Desktop): recoverable 0.
* **Aqeilan 2008 by plain E-utilities `efetch` (db=pmc)**: returns the front matter only; the file itself says the publisher does not allow the full text in XML form. **PMC article page**: a reCAPTCHA challenge page: a stop for that route. **Europe PMC fullTextXML**: timed out after 60 s. **Europe PMC PDF render**: HTTP 403 (a challenge page): a stop. The other five have no PMC id (checked with the ID converter), so no open route exists for them.
* Not used on purpose: any service that asks for a contact address (standing rule), any browser-header trick.

## 3. What the existing manifests already say about the rat-serum question (not verified against bytes)
The 2026-08-06 manifest of Suzuki 2009 carries three locators that bear on whether hypoglycaemia explains the rat's seizures: "Normal levels of serum constituents clearly excluded the possibility that these abnormal excitabilities are resulted from a systemic metabolic disorder"; "Postnatal earlier lethality in the KO mice seems to be related to their severely reduced serum levels of total protein, glucose and cholesterol as well as abnormal levels of electrolytes"; "By contrast, 28-day-old lde/lde rats had normal levels of these constituents". The manifest notes that the rat sentence is cited to Suzuki 2007 (PMID 17803050), whose abstract reports raised plasma urea nitrogen, creatinine and inorganic phosphate, so "normal" is narrower than it reads. (The ledger also holds a `complete_fulltext_read` of Suzuki 2007, `FTR-20260806-17803050-01`, whose bytes are absent from `files/fulltext/` too; the manifest's word "unread" for that source is not reconciled with it here.) These are quotes from a manifest, not from re-opened bytes: the same status the Baryla quotes had before their text was re-fetched. They stay a lead for the glucose line (a Wwox-deficient rat with seizures and, by this paper, no serum derangement at 28 days), not a result.

## 4. Next investment (HE57: a wait is not the answer; comparison written before the choice)
Candidates I could reach, each with what it could change and what it needs:
| Candidate | Could change | Needs | Why not first |
|---|---|---|---|
| **A. Audit gap on pending narrowing candidates** (the ADV-081 lesson: IT's revision carried one unaudited overshoot of mine; the 11-19 census of `commit_candidates/` shows 206 PROPOSED and 30 QUEUED, many without the word "audit") | whether a canonical claim is changed by a sentence that says more than its source; the mandatory audit triggers (narrow, reverse, remove a consolidated baseline claim) | a mechanical filter (status, target claim, audit mention), then a small sample read; no delegate until the list exists | overlaps IT's batch ownership: the output is a list for IT and ADV, not an application |
| B. PV population and maturation (portfolio RP-019, backlog) | which PV measurement the one-slot line names | complete primary reports and a formulated question | no laboratory is named and the v2 brief is not handed over, so the gain waits |
| C. Second animal-level source for the heterozygote latency | the last place in the measurement order | a literature search with a second route | the 11-19 search found none; no new trigger |
**Choice: A, as a bounded first slice** (the QUEUED candidates and any candidate that names a consolidated-baseline claim), reported as a list; B stays next; C waits for a trigger. The portfolio row to feed: RP-020 (harness simplicity) is not the right home; this belongs with RP-006 (batch diagnosis, repeated losses between reading and consumption).

## 5. Limits
My counts come from a header scan of `commit_candidates/` (status line and the words "audit"); the scan is a census, not a verdict on any candidate. The receipt facts are from `fulltext_read_receipts.jsonl` (events named by their own PMID), the byte facts from `evidence_presence.py`; I did not open any of the six papers.
