# SO_before_search - IT48-Q01 juvenile half, forward-citation route (written 2026-11-21 before any retrieval)

Role: producer (model sonnet, effort high, as stated at dispatch). Mechanism-level literature package; reference genotype class only. No dose, no recommendation.

## 1. The decision this question changes

Whether the first INV-18 arm must include the K2P or high-Ba2+ step (ladder step 2b), or can be reduced to the Kv7 spiking-range arm. A measured juvenile (P13-P17) Ba2+-sensitive share of resting conductance in L2/3 pyramidal cells at a low concentration (<= 50-60 uM, Kir2-selective range) that is small would mean the resting leak at that age is carried by something Kir2-selective Ba2+ does not remove (K2P or other), arguing for step 2b; a large low-Ba2+ share would argue that Kir2 carries the resting conductance and the arm reduces to the Kv7 spiking-range arm. No retrievable juvenile value leaves the decision where it is (not decided by this package).

## 2. What counts as FOUND (fixed now)

A paper is FOUND only if ALL hold, read in full text (Methods and the Ba2+ Results lines):
1. rodent (mouse or rat) neocortex (any area; entorhinal/hippocampus excluded), layer II/III or 2/3 (layer 2 alone and "superficial layers" recorded as near-miss, not FOUND), pyramidal (or explicitly excitatory principal) neurons;
2. age window stated that overlaps P13-P17 (a cohort window such as P12-P20 or P14-23 overlaps; a pooled cohort whose Ba2+ cells are not age-assignable is a near-miss, not FOUND);
3. Ba2+ or BaCl2 applied (any concentration; concentration is recorded and the answer is classed low <= 50 uM, intermediate 60-100 uM, high 100-500 uM, mM);
4. a share, a conductance fraction, or numbers from which one derives it (group means of Rin/Rm/input conductance/holding current before and after, with the same cells).

Concentration and age are recorded; a hit at another concentration is FOUND at that concentration, with the class stated.

## 3. Share versus current density

- SHARE (counts): Ba2+-sensitive fraction of resting (or input) conductance, of input resistance change expressed as conductance (1 - Rbefore/Rafter, group-mean arithmetic labelled DERIVED), or of holding current at a stated potential near rest.
- NOT A SHARE (recorded as a different denominator, never promoted): Ba2+-sensitive current density (pA/pF) or absolute current (pA) at a stated potential; percent block of the current at a strongly hyperpolarised potential (e.g. -130 mV); voltage-clamp Ba2+-sensitive I-V without a resting-conductance denominator; agonist-evoked current.
- Every candidates.tsv row states its denominator in a dedicated column. A value only in a figure/Extended Data is "figure-only, unread" unless the figure geometry is measured (method stated); never a number I did not read.

## 3b. Rejecting observation (pre-registered)

- Answer "no juvenile share exists in the retrievable literature": the seed citation set (seeds named in the brief plus R01-R13 of measurements.tsv; backward references and forward citations through OpenAlex and Europe PMC) is exhausted or screened to its limit, and no paper meets section 2 in full text, with every non-retrievable candidate listed for the supply list. Stated as two-route (OpenAlex and Europe PMC), never as proof.
- Answer "a share exists at a different age/concentration only": at least one paper meets items 1, 3, 4 and gives a share, but its age window does not overlap P13-P17 (e.g. P18+, adult) or the concentration is high/mM; reported with class and age, not combined into a gradient.
- Answer "FOUND": a paper meets section 2 fully; stop at the first one and report it (brief: stop at first candidate or when seeds exhausted).

## 4. What a negative result will and will not say

Will say: none of the papers connected to the seed set by direct citation, among those whose text I could read, contains a P13-P17 L2/3 pyramidal Ba2+ share; number of seeds, citing/cited papers screened, how many with body text read, how many unreachable.
Will not say: that no such measurement exists; that unreachable papers lack one; that papers not citation-linked to the seeds lack one. Screening of titles/abstracts chooses what to open and is never a verdict; a verdict needs Methods plus Ba2+ Results lines read in full text. Abstract-level conclusions are labelled abstract-level.

## 5. Route and conduct rules

- Routes: OpenAlex works API (public, no key, no e-mail, no mailto parameter, generic client name), Europe PMC REST citations/references, PubMed elink without e-mail, Europe PMC / PMC OA / bioRxiv copies for full text.
- A challenge page (captcha), 403, 429, 500 is a route result: recorded in SEARCH_RECORD.md, not bypassed, no browser-header spoofing, next route used.
- No e-mail address or personal detail is sent to any service. Zero spend. No agents started.
- IT49-Q09 side output: any source that falls out of the citation screen on which Kir2 subunits (Kir2.1/2.2/2.3/2.4) carry the neuronal Ba2+-sensitive current in cortical L2/3 pyramidal neurons goes to kir2_subunit_leads.tsv; not searched separately.
- Receipts: staged FULLTEXT_READ_RECEIPT JSON files in receipts/; the integrator records them (fulltext_receipts.py record is not run here). A receipt claiming complete_fulltext_read is made only when every section was read; otherwise partial_fulltext_read with missing sections named.
