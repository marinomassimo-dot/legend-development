# CC-20261004W10-Y-ARTEFACT-RECOVERY-01 — the artefact-absence condition on PMID 42397075 is discharged for the body and the main figures, and not for the supplement

`context_policy: SOURCE_FIRST` · intake wave 10, 2026-10-04, Scientist Y
**Change class: MINOR.** Nothing is reversed, no claim's `Status`, `Type`, `Summary`,
`Transferability` or `Source` moves. What changes is a stated *condition* on two landed records:
it is now partly met, and the part that is not met is named exactly.

## Why this exists

[[claim_registry_current#CLAIM 002]] and [[paper_registry_current#PAPER 001]] both record that a
blind locator audit of seven triples drawn from PMID 42397075 returned `UNVERIFIABLE_SURFACE` 7/7
**for absence of bytes, not on the merits**, and both state the condition that would unblock the
repointing of `CLAIM 002`'s `Source`: *a structured surface of PMID 42397075 acquired by any lawful
free route, re-read to receipt, with the five qualifications as verbatim locators*.

On 2026-10-04 an artefact was acquired — the author-accepted manuscript, CC BY-NC, 36 pp, from the
publisher's own open-access endpoint, free, no spend. The condition is therefore **no longer fully
unmet**, and the record should say which half moved.

## What was measured

- `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, sha256
  `9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b`, 36 pages.
- The artefact the earlier receipts declare (sha256
  `b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0`) is **absent from this host**:
  a SHA-256 search over `/home/desktop` and `/tmp/claude-1000` and a filename search over the whole
  filesystem returned nothing.
- **Same document, different bytes.** All six embedded figure images extracted from the new PDF
  reproduce the six figure digests the manifest already declared, **byte for byte**; all 15 body
  snippets the manifest declares occur **verbatim, exactly once each**, in text derived from the new
  PDF. The difference is a per-page access stamp carried on each of the 36 pages and dated at
  download time.
- 🔴 **Therefore this publisher endpoint is not digest-reproducible.** A download on another day
  yields a third digest for the same article. Verification here is by content, never by file digest.
- **Sixteen artefacts did not come back**, including the published supplement
  `brain-2025-03809-File009.pdf` and the thirteen images rendered from the supplementary figures
  volume. **Thirteen of the fourteen supplementary-figure locators of 2026-08-10 still quote bytes
  that exist nowhere.**
- Two of the five qualifications `CLAIM 002` names are **body** locators (*"rescued neuronal
  functional phenotypes without correcting RG abnormalities"*, Discussion; *"No randomization or
  blinding was applied in this study"*, Statistical analysis). Both verify in the new derived text.
  The three others live on figure surfaces, of which the main-figure ones are recoverable and the
  supplementary ones are not.

## Ops

### Op 1 — `paper_registry_current.md`, record `PAPER 094`, append to `**Evidence depth:**`

- `old` (measured unique in `PAPER 094`):
  `**Evidence depth:** complete_fulltext_read`
- `new`:
  `**Evidence depth:** complete_fulltext_read — ⚠️ **of an artefact that no longer exists.** The bytes that reading declares (sha256 \`b6b44816bb5a029ad6dd3760dbf02ae94c5fcb69f8a9b5721f45c128bbf189a0\`) are absent from every checkout and from the host. A replacement artefact was acquired lawfully and free on 2026-10-04 (\`files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf\`, sha256 \`9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b\`) and measured to be the SAME DOCUMENT, DIFFERENT BYTES: all six figure digests reproduce byte for byte and all 15 body snippets verify verbatim, while the file digest differs because the publisher stamps each page with the download date. 🔴 **Sixteen artefacts did not come back**, among them the supplement carrying the detailed Materials and methods, so thirteen of the fourteen supplementary-figure locators of that reading quote bytes that exist nowhere. complete_fulltext_read`

### Op 2 — `claim_registry_current.md`, record `CLAIM 002`, replace the unblocking condition

- `old` (measured unique in `CLAIM 002`):
  `**Cosa sbloccherebbe il ripuntamento:** una superficie strutturata di PMID 42397075 acquisita per qualunque via lecita e gratuita, riletta a receipt, con le cinque qualificazioni come locator verbatim.`
- `new`:
  `**Cosa sbloccherebbe il ripuntamento:** una superficie strutturata di PMID 42397075 acquisita per qualunque via lecita e gratuita, riletta a receipt, con le cinque qualificazioni come locator verbatim. 🔵 **Metà di quella condizione è soddisfatta dal 2026-10-04** (\`CC-20261004W10-Y-ARTEFACT-RECOVERY-01\`, intake wave 10): l'articolo è stato ri-acquisito dall'endpoint open access dell'editore — \`files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf\`, sha256 \`9775f766f68929e05665aa572196f4889083b501dc7f6792f1b9243e7dc0fd4b\`, CC BY-NC, 36 pp, nessuna spesa — ed è **lo stesso documento con byte diversi**: i sei digest di figura si riproducono byte per byte e tutti i 15 snippet di corpo verificano verbatim, mentre il digest del file differisce perché l'editore stampa su ogni pagina la data di scaricamento. **Le due qualificazioni di superficie \`body\` citate qui sopra sono quindi ri-verificabili oggi.** 🔴 **L'altra metà non lo è:** il supplemento pubblicato non è ottenibile per nessuna via lecita e gratuita raggiungibile da questo host — Oxford Academic risponde 403 dietro un interstiziale, non esiste deposito PMC (\`pmcid\` null, \`inPMC\` N, \`hasSuppl\` N, quindi \`pmc_pow_fetch\` non è applicabile), e il supplemento del preprint è un volume di figure *Expanded View* senza alcuna sezione di metodi. Finché resta così, le triple di superficie supplementare restano non ri-auditabili e il ripuntamento della \`Source\` resta **DEFERRED** per la ragione originale, non per assenza di tentativi.`

### Op 3 — `paper_registry_current.md`, record `PAPER 001`, append to the supersession note

- `old` (measured unique in `PAPER 001`):
  `no artefact of PMID 42397075 exists in this checkout and PubMed returns no PMCID for it`
- `new`:
  `no artefact of PMID 42397075 exists in this checkout and PubMed returns no PMCID for it — 🔵 **true on 2026-09-27, and half-corrected on 2026-10-04** (\`CC-20261004W10-Y-ARTEFACT-RECOVERY-01\`): the PMCID statement still holds, but the article itself was re-acquired free from the publisher's open-access endpoint and measured to be the same document, so a body-surface triple of that reading is auditable again; the supplementary-surface triples are not, because the supplement is still unobtainable`

## DEFAULTS_TAKEN

- The legacy artefact paths are **not** renamed and no manifest entry is deleted, although 16 of
  them point at bytes that no longer exist. Renaming or removing them would break the
  locator-to-artefact binding of readings already in the hash-chained ledger. The loss is recorded
  in the manifest's `artifact_continuity` block instead.

### LOCATOR TRIPLES FOR BLIND AUDIT

(Each artefact confirmed on disk before the triple was written.)

1. (The acquired artefact is the same document as the one the earlier receipts declare, and the digest difference is a per-page download stamp | `Downloaded from academic.oup.com/brain/advance-article/doi/10.1093/brain/awag239/8724067 by guest on 04 October 2026` | every page of `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, 36 occurrences in the derived text `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`)
2. (One of the two body-surface qualifications CLAIM 002 names verifies verbatim in the newly acquired artefact | `No randomization or blinding was applied in this study` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Statistical analysis)
3. (The published supplement is where the detailed methods live, which is why the article alone cannot supply them | `A detailed Materials and methods section is provided in the Supplementary material.` | `files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt`, Materials and methods, p. 4)
