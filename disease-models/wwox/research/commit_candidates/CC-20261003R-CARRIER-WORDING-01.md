# COMMIT CANDIDATE — CC-20261003R-CARRIER-WORDING-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist R), intake wave 5 2026-10-03, branch `task/sci-R-33914858`.
**context_policy:** `SOURCE_FIRST` — the heterozygote arm was read on the article's pages before any
LEGEND record or earlier candidate about it was opened.
**Not medical advice.** Class level only: a murine conditional heterozygote, no individual.

## Target

`disease-models/wwox/registries/claim_registry_current.md` · the **carrier claim proposed by
`CC-20261003W4-B-CARRIER-01`** (provisionally `CLAIM 045`; the propagating batch renumbers). One
clause of its `Bound` line is replaced.

🔴 **This candidate does not edit another actor's candidate file**, which is not mine to touch. It
proposes the repair to the *registry text* that candidate would create, and it is written so that the
integrator can apply it either (a) to the claim after `CC-20261003W4-B-CARRIER-01` propagates, or
(b) as an amendment to that candidate's `new` string before propagating it — the operator's or
integrator's choice. If the carrier claim is never created, this candidate expires with it.

## Why — one word of the bound is wrong, and it is wrong in the safe-sounding direction

The wave-4 bound reads, correctly on everything else: *"per l'eterozigote non è riportato alcun
endpoint di mielina, di imaging o comportamentale"* — no myelin, imaging or behavioural endpoint is
reported for the heterozygote **at all**.

The article's own page says otherwise for the behavioural half. It asserts a behavioural null:

> The heterozygote (*Wwox*⁺/flox, *Synapsin Cre*⁺) carrying one intact allele of *Wwox* did not show
> any abnormal phenotypes and was behaviourally indistinguishable from control mice.

There is **no datum behind it**: no n, no test, no assay named, no figure, no supplementary panel.
The Nestin heterozygote is treated the same way — *"did not show any visible abnormal phenotype"* —
and there the authors take the further step of transferring it to humans: *"which is in accordance
with the absence of neurological symptoms in heterozygous carriers in human individuals."*

So the correct bound is not *absent* but **asserted and not measured**, and the distinction matters
in both directions: a reader who believes the paper is silent may over-read a later behavioural
finding as filling a vacuum, and a reader who takes the sentence at face value may record a measured
negative where there is none. The myelin and imaging half of the wave-4 bound is **confirmed exactly**
by this full reading: nothing of the kind exists for either heterozygote.

A second, smaller repair: the wave-4 bound calls the Figure 2 legend's different denominators a
discrepancy. With both pages in hand it resolves — the legend counts **animals in which bursting
occurred** (3 of 14 S-HT, 20 of 24 S-KO), the text counts **slices** (4 of 23, 36 of 42). Both are
correct, and the claim should say so rather than leave a flagged inconsistency standing.

## Change class

**MINOR.** It replaces one clause of a bound in a claim that is itself proposed and not yet
canonical, making it narrower and more exact; nothing is reversed, no status changes. The triples go
to `legend-locator-audit` with those of `CC-20261003R-OKO-STRENGTH-01`, because the carrier claim
bears on `CLAIM 003`'s subject matter.

## Ordering

1. Receipt `FTR-20261003-33914858-03` in the ledger.
2. `CC-20261003W4-B-CARRIER-01` propagated (or its text amended in place by the integrator).
3. This candidate.

## Op list — `claim_registry_current.md` (record-scoped; **dry run NOT executed**; id provisional)

```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 045",
  "old": "e **per l'eterozigote non è riportato alcun endpoint di mielina, di imaging o comportamentale**.",
  "new": "e **per l'eterozigote non è riportato alcun endpoint di mielina o di imaging**. 🔴 **Sul versante comportamentale la formulazione va corretta (2026-10-03, `CC-20261003R-CARRIER-WORDING-01`, lettura integrale dell'articolo tipografico):** un endpoint comportamentale non è *assente*, è **affermato e non misurato**. Il lavoro scrive che l'eterozigote Synapsin *«did not show any abnormal phenotypes and was behaviourally indistinguishable from control mice»*, e dell'eterozigote Nestin che *«did not show any visible abnormal phenotype»*, in entrambi i casi **senza n, senza test, senza saggio nominato e senza figura**; nel secondo caso gli autori trasferiscono poi quel nulla non misurato ai portatori umani (*«which is in accordance with the absence of neurological symptoms in heterozygous carriers in human individuals»*). La differenza non è nominale: «silenzio» e «negativo dichiarato senza misura» si comportano in modo opposto davanti a un reperto comportamentale successivo. Si chiarisce inoltre che i denominatori diversi fra testo e legenda della Figura 2 **non sono un'incoerenza**: la legenda conta gli animali in cui il bursting è comparso (3 di 14 S-HT, 20 di 24 S-KO), il testo conta le fette (4 di 23, 36 di 42)."
 }
]
```

🔴 **No dry run was executed** (this worktree may not touch the four current files in any mode), and
the `old` string is the one `CC-20261003W4-B-CARRIER-01` proposes to write — it does not exist in the
registry yet. The integrator must re-measure it **after** that candidate propagates, or apply this
repair to that candidate's `new` string instead.

## What this candidate deliberately does NOT propose

- No change to the proportions themselves: 0/11, 4/23 and 36/42 are confirmed verbatim on the page.
- No change to the claim's `Status`, `Type` or `Transferability`, and no promotion of the carrier
  signal: there is still **no statistical test of either heterozygote against its control** anywhere
  in this paper.
- No statement about human carriers beyond recording that the authors assert the parallel.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The paper asserts a behavioural null for the Synapsin heterozygote without showing any measurement | carrying one intact allele of Wwox did not show any abnormal phenotypes and was behaviourally indistinguishable from control mice | PMID 33914858, Results, journal page 3065, `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf` PDF page 5 rendered at 110 dpi
2. The paper transfers the Nestin heterozygote's unmeasured normality to human carriers | did not show any visible abnormal phenotype, which is in accordance with the absence of neurological symptoms in heterozygous carriers in human individuals | PMID 33914858, Results, journal page 3065, same PDF, page 5 rendered at 110 dpi
3. The slice-level proportions are as the running text states them | In total, 0% S-Control slices showed bursting (0 of n = 11 slices across seven animals), 17% of slices from S-HT animals showed bursting (4 of n = 23 slices across 14 animals) and 86% of slices from S-KO animals showed bursting (36 of n = 42 slices across 24 animals). | PMID 33914858, Results, journal page 3065, same PDF, page 5 rendered at 110 dpi
4. The figure legend counts the same experiment by animal, which is why its denominators differ | four slices from three S-HT animals showed bursting | PMID 33914858, Figure 2 legend panel B, journal page 3067, same PDF, page 7 rendered at 110 dpi
5. Where the heterozygote enters a test at all, it is as the comparator of the homozygote | In vivo 12–20 Hz shows elevated power in S-KO as compared with S-HT and 7–15 Hz for S-KO as compared with S-Control | PMID 33914858, Figure 2 legend panel D, journal page 3067, same PDF, page 7 rendered at 110 dpi

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261003_005` · 2026-10-03 · ACTOR_ID `scientist` (Scientist J, batch integrator), under the operator's standing authorisation *«procedi sempre»*
**Operations applied:** 1
**Change class as judged by the batch:** MINOR (§7) — every target's live `Status` was read from the registry before judging.

`CLAIM 045` (`in observation`) — the clause *«non è riportato alcun endpoint di mielina, di imaging o comportamentale»* is narrowed to *mielina o imaging*, and the behavioural half is recorded as **asserted and not measured** rather than absent. The candidate's `old` string was re-measured in the live record first: `CLAIM 045` landed with `BATCH_20261003_003`, and the clause is present verbatim and unique. **Trimmed:** the candidate's second repair (the Figure 2 denominators) is largely already in the landed `Bound` line, so only its exact animal-level counts were added — three of fourteen S-HT, twenty of twenty-four S-KO, both verified on the rendered page — with the reconciliation labelled an `INFERENZA`, since neither surface states why the denominators differ. One audit amendment travels inside the claim: the two quoted sentences say nothing about whether a measurement was shown, so the absence of n, test and figure is recorded as an **earned zero** over the whole article and supplement.

**Nothing above this line was rewritten.**
