# Batch self-evaluation — `scientist-a`, AQEILAN-FT-A-001 wave 4, 2026-09-09

**The lot's last two readable papers: PMID 26499798 and PMID 31428585. Both complete, both audited.**

## Scope and executable verdict

| Gate | Result |
|---|---|
| `session_self_eval.py --disease wwox` | **PASS** — every complete read has landed and every declared output resolves. **Neither wave-4 PMID appears in any `[DECLARED GAP]`** |
| `deepdive_manifest.py --verify-artifacts --require-current-schema` ×2 | **PASS, 0 gaps** — 28 locators (26499798), 20 locators (31428585) |
| `fulltext_receipts.py verify` | **OK — 152 chained, tail anchored** |
| `legend_lint.py .` | **PASS** (one pre-existing INFO on CLAIM 010, not mine) |
| R4 | **Satisfied on both papers** — four blind auditors in total, all run before the respective commit candidates |

## Content diagnosis

**What the wave established.** On 26499798: a review that states its genotype–phenotype rule at
allele level while its own figure records three of six named variants in compound-heterozygous
genotypes — corroborating, from an independent source, the narrowing I made in wave 2 on `CLAIM 030`.
On 31428585: two unsupported forward clinical claims in a document with no data, one of which is about
the intervention class `DIS-003` rejects, filed as leads with their provenance and moving nothing.

**What it refused.** Q230P appears in neither paper (measured, zero occurrences in both). No mechanism
was carried, no molecule promoted, no claim status moved, and the one BLOCK-1-shaped item (Zfra) was
declared unrunnable rather than faked.

## Persistence diagnosis

**The one thing this wave got structurally right.** A session rate limit killed two auditors mid-run
and would have killed the session. I landed the 31428585 **reading** first — manifest, receipt,
dossier — and wrote **no commit candidate** until the audit had run, on the reasoning that *a landed
reading with no commit candidate touches no claim*. When the session resumed, nothing had to be
reconstructed. Wave 2 lost an audit to a session boundary and shipped locators marked `[UNAUDITED]`;
this wave lost two auditors to a harder failure and lost nothing.

**And when a wrong value was already persisted, it was corrected the lawful way.** The bad PMID sat in
an append-only ledger; it was fixed by a linked `receipt_correction` (`FTR-20260909-31428585-02`),
never by editing the JSONL.

## Process and capability diagnosis

**The wave's self-imposed target was met, and it is not where the damage was.** Wave 3 graded me
partial for not checking my most attractive finding as hard as my least attractive one. This wave I
checked the attractive finding first and hardest — the Figure 2B genotype work — and **it survived
two independent recomputations from the pixels, tick position by tick position.**

### 🔴 Where I grade myself down — three instances of ONE failure, and the target did not cover it

The target aimed at *the finding I most want*. **Every error this wave came from somewhere else: a
fact I never thought to doubt at all.**

| # | The error | How it was caught |
|---|---|---|
| 1 | Identified Figure 2A's markers as known phosphorylation sites. The article names **one** phosphosite; residues 12, 14 and 33 appear nowhere in its prose. **Background knowledge standing in for a source** — `DEFAULT_FROM_TEXTBOOK` used without declaring it, forbidden by `scientist_reading_modes.md` §3.3 | **Both blind auditors, independently** |
| 2 | Wrote two field-density counts from expectation: Zfra as 2 (it is **13**), Alzheimer as 36 (it is **32**) — and built a false sentence on the wrong one | **Me**, re-running before shipping |
| 3 | Gave ref 1's PMID as `29581896`. **The deposit's own markup carries `29310447`.** I ran an external author search and took its first hit **while the identifier sat inside the artefact I had open** | **Both blind auditors, independently** |

**These are one failure, not three: an assumption asserted with the confidence of a measurement, in a
place too small to look at twice.** Two were caught only because someone else looked. The honest
grade is **PARTIAL**, and the target for the next wave writes itself: *before a locator carries an
identifier, a count or a residue identity, the value must come from the artefact or from a command
run in this session — never from recall, and never from the first hit of a search.*

**The compensating observation, recorded because an audit that only reports failures is not an
audit.** Instance 2 was caught by me, before any auditor saw it, by re-measuring a number I had
written from memory. That is the wave-3 lesson working. And the audit's single most valuable output
across both papers was **not an error at all**: both auditors independently found a **second**
unsupported clinical claim in the editorial that none of my locators covered — weaker than the one I
had built the reading on, because it carries no attribution whatsoever. **The omission was the
finding.** A reading is not only judged by whether its propositions are true, but by whether the
document contains something worse that it walked past.

### One more thing to report, not to fix

`PMID 24550385` — read here at `complete_fulltext_read` since 2026-08-10 — **has no dossier**. Same
shape as `PMID 15070730` in wave 3, which had a complete receipt and no dossier until I wrote one.
It is not my paper and I have not touched it.
