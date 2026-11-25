# ADV-262 result: the three papers behind the claims' n that were not held (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. No spend, no contact, no e-mail address in any request, no claim file edited. Pre-registration: `PREREG_ADV262_SCI_20261125.md` (05:26:58Z, before any search). Downloads are in `files/fulltext/adv262_20261125/` (root checkout, not tracked).

## 1. Answer

| PMID | Paper | Route result | Unit of the n | Effect on the ADV-261 table |
|---|---|---|---|---|
| 34214506 | Saadane 2021, *Am J Pathol* | **Reached**: PMC article page (author manuscript, HTTP 200); Europe PMC `fullTextXML` answered 500; the PubMed full-text tool returned an empty text | "n = 2 replications of the results" (Figure 9 legend), one cone-photoreceptor line (661W), one siRNA supplier kit, two siRNA concentrations (5 and 25 pmol/L) | `034-01` becomes **non-independent** (replications of one cell line; derivation n = 1) |
| 17803050 | Suzuki 2007, *Comp Med* | **Not reachable by an open route**: not in PMC or Europe PMC, OpenAlex closed, no DOI, the stored copy of the 2026-08-06 reading is not on this host, SHA search of `/home/desktop` found nothing | the earlier reading recorded "n = 4 normal and 5 mutant per sex" (Table 2, 28-day-old rats); the litter of origin is not recorded | `038-01` stays **not checked here**; the record supports animals as the unit, litters unknown. Operator list, rank 16 |
| 40875931 | Gao 2025, *Neurology* | **Not reachable**: publisher answered 403 (Cloudflare challenge), not in Europe PMC, OpenAlex closed | the abstract (PubMed, not a read) states 50 individuals with biallelic variants across 45 families | `033-07` stays **not checked** for Table 2; the abstract alone says the cohort is not one individual per family (50 in 45). Operator list, rank 17 |

* **E1 (Saadane's n is replications, not independent): met.** The Methods say qPCR was run in triplicate, and the legend says "n = 2 replications of the results".
* **E2 (Suzuki's animals independent, litters not stated): not scored here**, because no text could be read; the earlier record agrees on animals.
* **E3 (Gao's families not stated or clustered): partly supported by the abstract only** (50 in 45).
* **E4 (at least one paper no open route reaches): met, two.**

## 2. Verbatim locators (Saadane 2021, PMC8579242, author manuscript)

* Figure 9 legend, panels B and C: "Wwox knockdown using siRNA inhibited the glucose-induced increase Wwox gene expression (B) and superoxide generation (C) as compared with cells treated with scrambled-siRNA. Data are expressed as means ± SD. n = 2 replications of the results."
* Results: "Cells treated with siRNA targeting Wwox gene inhibited Wwox mRNA by 65% compared with that in cells treated with scrambled siRNA (Figure 9 B), and significantly reduced the superoxide production in high glucose by 27% and 37% in the two different concentrations of siRNA (5 and 25 pmol), respectively".
* Methods, Cell Culture: "The authors used a cone photoreceptor cell line, 661W".
* Methods, qPCR: "PCR reactions were performed in triplicate and normalized to GAPDH."

## 3. What the claim should say (wording for IT, not applied)

`CLAIM 034`, where "n = 2" stands: "The loss-of-function evidence is two replications of one experiment in one cone-photoreceptor cell line (661W), with one siRNA kit at two concentrations and a scrambled control (Fig. 9 legend, PMC8579242); it has no independent derivation. The paper's first complete read is FTR-20260726-34214506-01 to -03; SCI re-read the n, the unit and the siRNA design on 2026-11-25 (partial, FTR-20261125-34214506-01)."

For `CLAIM 033`, add to the earlier ADV-261 line: "the 2025 Neurology cohort (PMID 40875931) is reported as 50 individuals in 45 families (abstract); Table 2 not re-read."

## 4. Limits

* The Saadane read is targeted (Methods and Results for the knockdown, Figure 9 legend); Discussion, other figure captions, tables and supplement were not opened. The receipt says so.
* No claim about Suzuki or Gao rests on a new read. The Suzuki figures come from the earlier reading's manifest, which names page 4 and the Table 2 row; the bytes are not on this host, so none of it was re-verified.
* Corrected route note: the brief listed the PubMed full-text tool as a route; it returned no text for an author manuscript PMC does not distribute as XML.
