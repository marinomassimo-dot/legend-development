# CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01 — four published quantities in this wave cannot be carried as printed, and one of my own extractions was wrong the same way

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-03 · **Author:** Scientist C, intake wave 5 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead);
no canonical claim is narrowed or reversed, so this is MINOR by §7 of the batch protocol.

---

## 1 · The finding

Wave 4 established that figure panels change summary sentences, usually weakening them. This wave
found the adjacent failure: **published quantities that are internally contradictory or
typographically impossible, in four places across two papers, plus one defect I introduced myself by
reading a numeric table from flattened text.** Every one would have produced a wrong carried number
had the panel or the cell structure not been inspected.

| # | Source | What is printed | Why it cannot be carried |
|---|---|---|---|
| 1 | PMID 41966056 | `1E−10 vector genome copies/g brain mass (1.265E−13 genome copies)`, in **both** abstract and body | A negative exponent denotes a fraction of one genome copy. The superscripts were lost at typesetting. The intended magnitudes are recoverable only by the paper's own internal division, which yields a brain mass in grams plausible for the recipient's age band; no reading of the printed negative exponents yields a mass at all. |
| 2 | PMID 41948127 | low NHP dose `6E13 total vg` in Results **and** Methods; `5E13 vg` in the Figure 5A row labels | Two different values for the same dose in the same paper. Verified at 800% magnification of the rendered panel. |
| 3 | PMID 41948127 | `a single 4-mL intrathecal infusion` (Results) vs `a 3-mL single-dose intrathecal slow infusion` (Methods) | Infused volume relative to CSF volume is the quantity PMID 42205472 identifies as governing delivered dose at target, so this is not cosmetic. |
| 4 | PMID 41948127 | Figure 5A scale bars `300 mm and 600 mm` in the caption; the panel prints `300 μm` and `600 μm` | The caption's unit is wrong by three orders of magnitude. A locator drawn from the caption would have been wrong; the panel is right. |
| 5 | PMID 42134074 | `9.3% ... IT treated ... 9.8% ... sham-control ... in comparison to IT delivery (2.7% ... and 2.0% or the sham-control ...)` | Compares one route to itself; gives a sham-control rate exceeding the treated rate; contains a typographical error. At least one "IT" must be "IV" and which cannot be recovered. **None of the four percentages is usable.** |

### And one defect of my own, recorded because it is the same failure mode

Reading PMID 42205472's Table 4 from a **flattened** JATS text rendering — in which adjacent numeric
cells concatenate without a delimiter, e.g. `Rat2.2200.1519.5` — I produced a plausible but wrong
table and drafted a criticism of the source for an internally implausible cell. Re-extracting
**by cell boundary** from the XML gave `Rat | 2.2 | 20 | 0.15 | 1 | 9.5` and showed the source is
correct and self-consistent. **The defect was in my extraction, not in the paper.** Had I not
re-read it cell-wise, this wave would have published a false negative finding against a source.

## 2 · Why this belongs in the ledger rather than in six dossiers

Each instance is recorded in its own dossier. What is reusable is the **rule**, and the rule has now
been earned twice from different directions: wave 4 found captions understating panels, wave 5 found
printed quantities contradicting panels, contradicting each other, and surviving my own extraction
incorrectly. A single lead captures it.

## 3 · Op — discovery_ledger_current.md

`op: APPEND` one lead at the end of the lead list of
`disease-models/wwox/research/discovery_ledger_current.md`. There is no `old` text; this is an
append.

```
### DIS-xxx (provisional) — A carried quantity is not verified until it has been read in the form the publisher rendered it

**Tag:** INFERENZA (method)
**Status:** open
**Created:** 2026-10-03 · intake wave 5, Scientist C (group C)
**Causal statement:** A number taken from a paper's running text or from a figure caption is an
unverified transcription of that number until it has been checked against the structure that
actually carries it — the rendered panel for a figure value, the cell boundaries for a table value.
In six readings of AAV9 delivery-safety literature this check changed or invalidated five published
quantities and caught one defect introduced by the reader's own extraction.
**Reasoning chain:**
1. Two papers printed a quantity in two mutually exclusive forms (a dose as both 6E13 and 5E13; an
   infusion volume as both 4 mL and 3 mL), each time with the figure panel disagreeing with the text.
2. One paper printed a dose with a sign that is physically impossible, identically in abstract and
   body, so no amount of cross-reading within the text would have caught it; only arithmetic on the
   paper's own paired values recovered the intent.
3. One figure caption gave scale bars in millimetres where the panel printed micrometres.
4. One review paragraph printed four percentages in a comparison that compares a route to itself.
5. The reader's own first pass at a numeric table, read from flattened JATS text where adjacent
   cells concatenate without a delimiter, produced a wrong table and a false criticism of a correct
   source; cell-wise re-extraction corrected it.
**Counter-evidence / what would refute this lead:** a sample of carried numbers in which panel-level
and cell-wise verification changes nothing, i.e. a body of literature where running text, captions
and panels agree. Nothing in waves 4 or 5 suggests that body exists, but neither wave sampled
randomly — both read papers selected for a safety question, and typographic care may differ by venue.
**Falsifying experiment:** take a random sample of 20 quantities already carried in the WWOX paper
registry whose sources are held locally, re-verify each against its panel or table cell, and count
discrepancies. The lead predicts a non-trivial rate; a rate of zero refutes it.
**Operational consequence (proposed, not a gate):** when a quantity is to be carried into a registry
record, a claim or a candidate, read it in the structure that carries it — render the panel, or
extract the table by cell — and quote the command that produced the figure. Where a source prints a
quantity in two forms, carry neither silently: carry both with the discrepancy named.
**Links:** `research/intake_wave_20261003w5_C.md` §9; dossiers `PMID41966056.md` §3,
`PMID41948127.md` §6, `PMID42134074.md` §7, `PMID42205472.md` §3.
**Not medical advice.**
```

## 4 · What this does NOT propose

- No gate, no LINT rule, no ratchet. Wave 4's lesson and this one are two samples; a gate built on
  two non-random samples would fire on honest work.
- No correction to any existing registry record: none of the five defective quantities has ever been
  carried into this repository, because all six sources are first readings with no prior registry
  presence.
- No claim that these sources are unreliable overall. Three of the five defects are typesetting, and
  the sixth was mine.

## 5 · LOCATOR TRIPLES FOR BLIND AUDIT

```
(The dose is printed with a negative exponent of vector genome copies per gram of brain mass, in the body of the article | Following successful computed tomography (CT)-guided access to the cisterna magna with a 25-gauge neonatal spinal needle, 1E−10 vector genome copies/g brain mass (1.265E−13 genome copies) of RGX-111 in 5 mL of Elliotts B artificial CSF was injected over 5 min without adverse effects. | files/fulltext/PMID41966056_Wang2026_PMC.xml — Results, 'Clinical outcomes', dosing paragraph)

(The running text of the article states the low non-human-primate dose as 6E13 total vector genomes | To perform this experiment, 20 wild-type monkeys (10 males, 10 females) were randomly assigned to one of three dose groups (control, formulation buffer, N = 4; low-dose [6E13 total vg] and high-dose [1.2E14 total vg] AAV9.U6.miR871) (N = 8 animals per group). | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Results, 'Intrathecal delivery of AAV9.U6.miR871 to non-human primates')

(The methods section of the same article states the infusion volume as 3 mL where the results section states 4 mL | Animals were mildly sedated with 10 mg/mL acepromazine, and test article was administered to each animal as a 3-mL single-dose intrathecal slow infusion over approximately 6 h via a pre-study implanted catheter. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Materials and methods, 'NHP study design')

(The results section of the same article states the infusion volume as 4 mL | Vector or formulation buffers were administered via catheter, implanted pre-study, as a single 4-mL intrathecal infusion over a 6-h period to avoid increasing intracranial pressure. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Results, 'Intrathecal delivery of AAV9.U6.miR871 to non-human primates')

(The figure caption states the panel A scale bars in millimetres | (A) H&E staining of representative dorsal root ganglia (DRG) from miR871-treated animals show no significant histological abnormalities compared to control. Black boxes in left panel are shown at high power in the right panels. Scale bars: 300 mm and 600 mm. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Figure 5 caption, panel A)

(The review paragraph reporting hepatotoxicity frequencies compares one route to itself and gives a sham-control rate exceeding the treated rate | Side–effect profile was favourable and similar to that seen with earlier IV studies (9.3% for the OAV101 IT treated patients and 9.8% for the sham-control treated patients hepatotoxicity), in comparison to IT delivery (2.7% for the OAV101 IT treated and 2.0% or the sham-control treated patients) but with two notable cases of sensory symptoms that are suggestive of DRG toxicity. | files/fulltext/PMID42134074_Kagiava2026_PMC.xml — Clinical applications, 'Spinal muscular atrophy (SMA)', STEER paragraph)
```

**Artefacts confirmed on disk before writing these triples:**
`files/fulltext/PMID41966056_Wang2026_PMC.xml` (sha256
`d742797b9570be3b99d8d2279763e11f7f1f369135a6dd7ee96d50392ce22ed8`),
`files/fulltext/PMID41948127_Stavrou2026_PMC.xml` (sha256
`97cb20ba89331fbbed6256c401b3f828a58a26c7e7f685f769da135ca026003b`),
`files/fulltext/PMID42134074_Kagiava2026_PMC.xml` (sha256
`04ccc505a3beafee422bed0f57872d8b989a8f948becc61aaf3de5469444a1d5`),
`files/figure_renders/sciC_w5/PMID41948127_fig5.jpg` (sha256
`b9ddaacc19869f4368871e24048397b47766eea71c69fd3badbd4ad96a89146c`).

> The auditor is asked to judge only whether each quote supports its proposition and whether the
> source says more or less than the proposition claims. The panel values that contradict triples 2
> and 5 are in the declared figure render, which the auditor should open.
