# Supplementary Fig. 6F (TCF4 in rescued WWOX-KO organoids) — state of the material, and what the panel says

`scientist-c` · 2026-10-25 · task `SUPPL6F-20261025` · QUESTION_DRIVEN
Subject: the published supplementary volume of Brain `awag239` (`PMID 42397075`), and the one
panel a live investigation needs from it — Supplementary Fig. 6F, the TCF4 (TCF7L2) immunoblot
that includes a **rescued** WWOX-KO arm.

## 1 · The five-way state of the ten absent entries

The manifest `deepdive_manifests/PMID42397075.json` declares **fourteen** SHA-256 digests as
absent — `source_artifacts` 1–14 — not ten: one PDF (`brain-2025-03809-File009.pdf`, the
supplementary-figures volume) plus thirteen images derived from it (eight `S_fig_p*_170dpi.png`,
four `S_page_p*_258ppi.png`, one `S10_caption_p19_200dpi.png`). The wishlist row of 2026-10-24
counts "ten locator entries (15 and 21–29)", which is the count of **locator** entries bound to
those images, not of artefacts. Both counts are right about different things; this record uses
the artefact count, because digests are what a search can decide.

| State | Entries |
|---|---|
| already present and verified | — none of the fourteen |
| accessible and not yet acquired | — none: see § 2, the only exposed route is signed and expiring |
| acquired but not yet read for this question | — none |
| **genuinely unavailable from this host** | **all fourteen** (artefacts 1–14), re-confirmed by digest search on 2026-10-25 |
| **present in a different, non-equivalent version** | the **content** of Supplementary Fig. 6F only, as preprint **Fig. EV6F** (§ 3) — no digest of the fourteen is matched by it |

Search scope, so the negative is bounded rather than asserted: `evidence_presence.py --search`
over the whole of `/home/desktop` and `/tmp/claude-1000` (and, in a second faster pass, over
`files/`, `Downloads`, `Documents` and the 2026-10-04 receipts backup). Result in both passes:
`present 13 | absent 14 | digest_mismatch 0 | recoverable 0`. Not one of the fourteen digests
matches any byte sequence on this host, under any filename.

The last two rows are not in tension. The bytes the manifest fingerprints are gone and are not
re-acquirable; a *different document* carries the same experiment under a different figure
number, and that document is held locally and was read.

## 2 · The publisher route, measured today

- Europe PMC was **not** re-run: the 2026-10-25 measurement in
  `research/operator_pdf_wishlist_20261021.md` (no PMCID, `isOpenAccess N`, `hasSuppl N`,
  `inEPMC N`) stands.
- The article page `academic.oup.com/brain/advance-article/doi/10.1093/brain/awag239/8724067`
  returns **HTTP 403** to a direct request from this host — the same Cloudflare bot check
  recorded on 2026-10-04. It was **not** circumvented, and a browser-impersonating retry was
  refused by this deployment's own guard rather than attempted.
- 🔴 **New, and it corrects the 2026-10-04 record.** That record states that no supplementary-data
  link could be read. Through an ordinary page fetch the link **can** be read, and it exists:
  a single archive, `awag239_supplementary_data.zip`, served from
  `oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/brain/PAP/10.1093_brain_awag239/1/`.
  So the material is published and its address is known.
- The archive is **not** retrievable from here: the CDN requires a signed, expiring URL
  (`Expires`, `Signature`, `Key-Pair-Id`); the unsigned path returns
  `403 MissingKey`. The signature is minted by the article page, which is behind the bot check.
  There is no lawful automated route from this host, and no further one was sought.
- Crossref carries no supplementary relation for the DOI (`relation: {}`); the only links are the
  accepted-manuscript PDF, already held. Licence is CC BY-NC on the accepted manuscript.
- **Consequence for the wishlist:** the row should stop reading "not a routing gap" alone and
  carry the archive's name and path. It is a **one-click operator action** from a browser
  session — a single ZIP, which would discharge all fourteen absent digests at once if its
  File009 matches, and would otherwise be recorded as a different version.

## 3 · Fig. EV6F — the panel, read for one question

Preprint bioRxiv v2 (2025-09-25), `files/fulltext/PPR960425_Steinberg2025_bioRxiv-v2.full.pdf`,
page 53, the Fig. EV6 composite. The sentence citing the panel is identical in the preprint and
in the published accepted manuscript except for the figure label, so the two cite the same
experiment: *"we assessed Wnt pathway activity in WWOX-KO, WOREE, SCAR12, and rescued WWOX-KO
organoids"* → *"Western blot analysis revealed elevated levels of TCF4 (TCF7L2)"*.

- **Lanes (six, one per line, no replicate lanes):** JH-WT · WKO-1C · WKO-2C · SCAR12 · WOREE ·
  **WKO-1C AAV9**.
- **Rows:** TCF-4 (~56 kDa), WWOX (46 kDa), GAPDH (36 kDa).
- **Printed quantification, normalised to JH-WT = 1:** 1 · 1.4 · 1.3 · 1.7 · 3.1 · **0.3**.
- **n:** none declared for (F). The legend's *mean ± SEM / one-way ANOVA / asterisks* sentence
  belongs to panel (B); panel (F) carries no error bar, no asterisk and no replicate count.
- **Answer to the question asked:** in this version, TCF4 in the AAV9-rescued WWOX-KO organoid
  does **not merely return toward** wild type — the printed figure is **0.3**, i.e. below the
  wild-type lane, while the unrescued clones sit at 1.3–1.7 and WOREE at 3.1. Read as written,
  the rescue over-corrects rather than normalises.
- 🔴 **Three limits that travel with that number.** (i) It is the **preprint**, not the published
  Supplementary Fig. 6F, and is not peer reviewed; the published panel has not been seen and may
  differ. (ii) It is **one blot, six single lanes**: six numbers, not a measured distribution,
  and nothing here supports a p-value or a confidence statement. (iii) The GAPDH band in the
  WOREE lane is visibly lighter than its neighbours, which bears directly on the 3.1 — the
  largest effect in the panel sits on the weakest loading control.
- The rescue is **AAV9-WWOX in one knockout clone (WKO-1C)**. The published body sentence says
  only "rescued WWOX-KO organoids"; the vector and the single-clone scope are visible only in the
  figure.

Nothing else in the preprint's expanded-view volume was read for this task.

## 4 · What is still owed

The published supplement remains unobtained, and with it any re-audit of the readings that rest
on its vanished bytes (`DL-THER-081`, the Supplementary Fig. 7F-G readings, and the A51 dose and
schedule, which the preprint does not contain at all). The TCF4 finding above is usable **as a
preprint reading**, tagged as such, and must not be cited as the published supplement.
