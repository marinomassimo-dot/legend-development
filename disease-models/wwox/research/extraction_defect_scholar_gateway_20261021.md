# Measured scope of a hyphen-stripping extraction defect — Scholar Gateway surfaces, 2026-10-21

**Orchestrator · READ-ONLY measurement · no canonical file changed · not medical advice.**
Provoked by the blind locator audit of PMID 36537114
(`page_adjudications/locator_audit_PMID36537114_20261021.md`, commit `545dd670`), which found that
a growth value could not be verified for its sign and reported that "every hyphen in the document is
gone". That is the right alarm and the wrong scope, and both halves matter, so this note measures it.

## 1 · What the defect is

In the two persisted surfaces of PMID 36537114 — `files/fulltext/PMID36537114_Chong2023_ScholarGateway_20260929.json`
and `files/fulltext/PMID36537114_Chong2023_SGchunks_text_2026-10-21.txt`, both fingerprinted in
`deepdive_manifests/PMID36537114.json` — hyphens **inside words** and **minus signs before numbers**
are absent, while the hyphens of the table scaffolding survive. Measured:

| Token the source must contain | Occurrences | Glued form present |
|---|---:|---:|
| `short-chain` | 0 | `shortchain` 3 |
| `loss-of-function` | 0 | `lossoffunction` 2 |
| `exons 6-8` | 0 | `exons 68` 1 |
| `50th-75th` | 0 | `50th75th` 2 |
| `34 weeks` / `3-4 weeks` | 0 | `34weeks` 1 |

A first check that counted hyphens file-wide was **misleading and is recorded as such**: the `.txt`
holds 192 ASCII hyphens, all in table pipes, dates and identifiers. A file-level count cannot see
this defect; only the token shapes can.

**Why it is dangerous rather than untidy.** The growth row reads `OFC: 2 SD`, `Weight: 1.5 SD`,
`Height: 3.0 SD`. In a WOREE case series those are deficits — three standard deviations *below* the
mean — and the stripped surface renders them as magnitudes that a reader, or a script, can take for
values above it. A sign is not a formatting detail: it reverses the finding.

## 2 · Measured scope: one study, not the corpus

Scanned every file under `files/fulltext/` larger than 2,000 bytes. Two passes:

- A loose signature (common glued compounds) flagged 62 files, and it is **not usable**: `wildtype`,
  `followup` and `longterm` are legitimate single-word spellings in published text. Reporting those
  62 as defective would have been a false alarm of exactly the kind this note exists to prevent.
- A strong signature — nine token shapes that can only arise from a removed hyphen, requiring **two
  or more distinct** shapes in one file — returns **3 files**: the two surfaces of PMID 36537114
  (7 distinct shapes, 31 hits each) and `PMID16187332_Thavathiru2005.html`, which is a **false
  positive**: its matches sit inside URL-encoded strings (`%20weeks`) and the file carries 3,739
  hyphens. 522 files show no signature at all.

**So the defect is confined to the Scholar Gateway route's output for this one paper.** Exactly one
manifest in the repository cites that route (`PMID36537114.json`); no other reading rests on it.

## 3 · What follows, and what does not

- **No signed, ranged or hyphen-bearing value from these two surfaces is verifiable**, and the audit
  correctly returned UNVERIFIABLE rather than a finding against the reading. The other eleven triples
  verified against the same surfaces held: the defect bounds which *kind* of token is unreliable, not
  the reading as a whole.
- **A native-resolution surface for DOI 10.1002/ajmg.a.63074 must be re-acquired** before any signed
  value from this paper is used. Earlier cascades recorded this paper as having no lawful free route,
  so it belongs on the operator's PDF list; an access control is not to be circumvented.
- **Route-level caution for the next reader, which is the transferable part:** a surface obtained
  through Scholar Gateway must have its token shapes checked before any signed or ranged number is
  taken from it. The nine-shape test in § 2 is the check, and it is cheap.
- **What this does NOT license:** no claim about the Scholar Gateway service in general (one paper is
  one observation), no inference that other routes are clean beyond the scan reported here, and no
  change to any claim. The scan covered `files/fulltext/` only — page renders, supplements and
  figure extractions were not examined.

## 4 · Commands, so the measurement can be repeated

The two scans of § 2 were run inline over `glob.glob('files/fulltext/*')` with the loose and strong
signature sets quoted above; the per-token counts of § 1 were taken from the `.txt` surface named
there. Re-running them needs no network and no credential.
