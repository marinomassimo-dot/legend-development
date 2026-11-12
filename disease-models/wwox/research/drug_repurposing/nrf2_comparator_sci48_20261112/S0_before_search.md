# SCI48 S0 — which KEAP1/NRF2 comparison can tell an NRF2-dependent effect from another action in a neural system: frame, priors and stop rule, written before any new search (2026-11-12)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX; no compound is promoted. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI. Task record `ledger/tasks/orchestrator/ORCH-SCI48-20261112.json`. A later change to this file is a dated addendum, not an edit. Paths are relative to `disease-models/wwox/research/drug_repurposing/`.

## 1 · State found (reconciled, not re-opened)

* **SCI46** (package P and the expression item) and **SCI47** (A inhibitory defect; B cell context; tail) are landed on `main` and consumed in part by IT47 (`generation_it47_20261112/p2_sci46_it47.md`). Nothing of them is repeated here.
* **Open questions still open on 2026-11-12** (`batch_sci_20261105/map/open_questions_map.tsv`, rows read today): IT46-Q06 (Winkel 2015 full text and its knock-out verification; status OPEN, "full text returned an error twice; not retried by another route") and IT46-Q09 (sulforaphane with a null arm in neural cells; OPEN, untested). Neither is assigned elsewhere: `next_batch_it47_20261112/BRIEFS.md` B5 lists both as literature-executable, zero spend, and no ledger task names them. IT46-Q02 (the target named ABAT in the EUbOPEN panel) is also open and is the optional tail.
* **Dated corrections that bind this work.** SCI46 `README.md` carries the V8 corrections (the producer's "inadequate knockdown" for LUHMES was withdrawn; "near-baseline" NQO1 was 0.2–0.5; Wu's ">95%" is about 86–92% by figure read). IT47 P2 added the dated correction to V19 ("no neuron or astrocyte data exist for any of these compounds" was too strong for the covalent class; it stands for the non-covalent binder). The old IT45 sentence is not the current state.
* **What the SCI46 packet read and at which depth** (so it is not read again as if new): Davies 2016 (27031670) only as ChEMBL transcription [CH], text closed; Wu 2024 (39497026) full text, figures 5 and the occlusion arm viewed, others not; Costa 2024 (39209951) partial full text with Fig 1, 6 and Supp S4 viewed; Tran 2019 (31411465) partial full text; Singh 2016 (27552339) partial; Winkel 2015 (26459563) **abstract only** (PubMed tool; Europe PMC XML HTTP 500 twice, the PubMed tool returned empty); Kraft 2004 (14762128) abstract only after four routes; Linker 2011 (21354971), 30587509 and 37187090 abstract or [CH]; Zhu 2025 (40021790) full text by keyword scan. Sulforaphane: **no source in the packet** (it was inactive in the Kelch FP assay of 31411465; absent from 38116420; potency rows only in 37187090 at abstract/[CH]).

## 2 · The decision this can change

`compound_view.tsv` row V19 and INV-08 steps X0–X3 currently pair "a covalent KEAP1 modifier and a non-covalent binder, told apart by a knockdown of NRF2". Today the pair has: one non-covalent binder (KI-696) whose knockdown arms are unreadable (Davies, categorical labels), inadequate (LUHMES) or glial (Wu); a covalent comparator list (sulforaphane, dimethyl fumarate, bardoxolone methyl) whose derived roles are `NONE` or `ABSTRACT`; and a second binder (RA839) with no role at all. The decision is therefore: **which reagent may be written into the INV-08 comparison as (i) an NRF2 probe, (ii) a comparator, (iii) a conditional hypothesis, or (iv) not interpretable**, and which loss arm and readout classes the comparison must carry for that role to hold. A role is a statement about the reagent, not about WWOX.

## 3 · The question and the two entry points

Which comparison — a non-covalent KEAP1/NRF2 binder, an electrophile already used as comparator, and a genetic or orthogonal control — can separate an NRF2-dependent effect from another action in a neural system, and within which limits?

* **A. Winkel 2015 (RA839).** Does the full text, with its controls, qualify RA839 as a comparator: how NRF2 loss was produced and verified, whether the covalent comparator (CDDO-Me) was run in the loss arm, what the two genes that survive in the knock-out are, binding evidence and exposure, cell class (myeloid, not neural), viability control.
* **B. Sulforaphane with NRF2 loss in neural cells.** Which sources exist, what loss was used (germline knock-out, shRNA/siRNA, dominant negative), whether the loss was verified at the endpoint time, and which endpoint each reports: **molecular** (ARE reporter, target mRNA/protein), **viability**, **function** (electrophysiology, network, behaviour, cytokine release is molecular).

Both stay as given because both answer the same decision. If reconnaissance shows another source answers it better, the reason is written as a dated addendum below **before** the perimeter is widened.

## 4 · Three claims kept apart

1. A reagent acts **through** NRF2 (loss arm adequate at the endpoint time, occlusion by KEAP1 loss, matched on-target response).
2. That direction is **useful** in the loss of WWOX (a WWOX-deficient neural preparation; nothing read so far has one).
3. The result **transfers** to a therapeutic proposal (exposure, brain access, safety). Proof of (1) resolves neither (2) nor (3).

## 5 · Which outcomes would favour which explanation, and which would leave the comparison uninterpretable

| Outcome (per reagent, per endpoint class, per cell class) | Favours | Does not allow |
|---|---|---|
| Effect lost under a loss shown adequate at the endpoint time (target protein/mRNA and a target gene) | NRF2 dependence **of that endpoint** (H1/H3) | absolute specificity; dependence of other endpoints |
| Effect maintained under an adequate loss | an alternative route (H5): the reagent is not an NRF2 probe for that endpoint, may still be a lever | "NRF2-independent" for other endpoints |
| Effect maintained or reduced under a partial or unverified loss | nothing | dependence or independence |
| Germline knock-out only | dependence in a compensated, developmentally altered cell | the acute-loss reading; neuronal vs astrocytic origin if mixed culture |
| Covalent and non-covalent reagent in one loss arm, one cell type | a within-paper contrast of classes | a match on on-target response unless both were measured |
| Reagent exposure toxic or far above the on-target range | the survivor set after loss may be toxicity | a specificity statement |
| Only NQO1, or only one gene, as the molecular endpoint | a weak molecular reading (SCI46 P8) | a mechanism readout |

The comparison is **left uninterpretable** if: no source pairs the reagent with an NRF2-loss arm in a neural or glial class; or every loss arm is partial, unverified or germline-only without an occlusion arm; or the endpoint differs between the reagents of a pair. In that case the finding is "no available reagent is a good comparator in this class" and the experiment is stated as the minimum that would make one.

## 6 · Priors, fixed before searching (recollection or inference; unverified; scored afterwards, may fail)

* **S1.** The Winkel 2015 full text is open in PMC and reachable by the PubMed full-text tool or the PMC route used before; the earlier HTTP 500 was transient.
* **S2.** In Winkel, NRF2 loss is a germline knock-out in bone-marrow-derived macrophages, and its adequacy is shown by absent target-gene induction (and possibly absent protein), not by an acute-loss verification.
* **S3.** CDDO-Me was **not** run in the knock-out arm; the knock-out arm carries RA839 only. If true, the within-paper class contrast exists for the wild-type response (both prevent iNOS induction) and not for specificity.
* **S4.** RA839 has no use in a neuron, astrocyte or microglia in the literature reached by title/abstract search; Winkel stays myeloid.
* **S5.** For sulforaphane in neural cells there are several papers with a germline Nrf2-null or knockdown arm; most report molecular and viability endpoints; **none** reports a functional endpoint (electrophysiology or network) with an adequately verified loss.
* **S6.** Where sulforaphane has a null arm in neurons or astrocytes, ARE gene induction and oxidative-stress viability protection are lost; some anti-inflammatory endpoints in microglia persist (mixed result).
* **S7.** Most sulforaphane neural sources use concentrations in the micromolar range (about 1–20 µM) at which documented thiol-reactive actions beyond KEAP1 (HDAC, NF-κB, heat-shock response) are possible, so the persisting effects after loss cannot be assigned without a second reagent class.
* **S8.** No single source holds sulforaphane and a non-covalent KEAP1 binder in one loss design in a neural class (the SCI46 prior P7 held for neural cells; it failed at database depth in NHBE epithelium).

## 7 · What no reading can resolve (stated now)

Whether NRF2 is insufficient, already induced or compensating in a WWOX-deficient neural cell; whether any KEAP1/NRF2 intervention improves a WWOX-relevant function; brain exposure of any reagent; whether a loss that is adequate in a macrophage or an astrocyte is adequate in a neuron. These need the premise measurement (INV-08 X0) and the arms X1–X3; this package defines which reagent role each source can support and the minimum comparison that would make a role interpretable.

## 8 · Perimeter, depth rule and stop criterion

* **Access.** Plain tools only, default user agent; PubMed/PMC tools, Europe PMC REST, ChEMBL REST, PubChem/RCSB as in SCI46. A bot check, 403 or 429 is recorded as unreachable and not retried by another route. Winkel: the Europe PMC XML and the PubMed full-text tool are retried **once** each, because the 500 is a server error 19 hours old and the earlier two attempts were minutes apart; a second failure is recorded as a technical block and closes the question for this package without another route.
* **Depth.** Text, figures and supplements opened for every source that carries a decisive proposition; depth stated per source in the receipt (`fulltext_read_receipt.md`); an abstract is a pointer, not a read; a partial read is never written as complete.
* **Search.** Winkel: the paper, its figures and any supplement. Sulforaphane: Europe PMC and PubMed strings (sulforaphane AND Nrf2 loss terms AND neural terms; strings and counts logged), titles/abstracts of at most 40 candidates screened, at most 8 opened beyond the abstract, chosen by the criteria in the brief (neural class; loss arm; endpoint class), with the exclusions named. One revision of the strings is allowed if the first returns fewer than 10 candidates, and the revision is logged.
* **Stop.** Stop when (a) Winkel is read or its block is recorded, and (b) either two neural sulforaphane sources with a loss arm are classified by endpoint class, or the logged strings show none. No widening to a catalogue of compounds; a third reagent enters only if a source reached in passing is the one pairing a covalent and a non-covalent reagent in one loss design in a neural class, and then it is added with its reason.
* **Delegation.** One producer (`legend-delegate`, sonnet, medium) and one blind verifier (sonnet, high) with the full originals; settings read back from the transcripts with `session_model_census.py`; no recursive agents.

## Addendum 2026-11-12 17:15 UTC — access to Winkel 2015 (dated; the sections above are unedited)

Per the stop rule of section 8, the Europe PMC `fullTextXML` request for PMC4653701 and the PubMed full-text tool were retried once each: HTTP 500 again (third failure of that endpoint over two days) and an empty `full_text` with the abstract only. That closes those two routes. A different **public mode that SCI46 never tried for this article** was then used once, with the default user agent: the PMC article page `pmc.ncbi.nlm.nih.gov/articles/PMC4653701/` returned HTTP 200 with the body (59,441 characters of text after stripping markup; Results, Experimental Procedures and Discussion present) and nine figure images from the PMC image host. No block (bot check, 403, 429) had been met for this article, so no refusal was bypassed. The PMC supplement URL returned the "Preparing to download" interstitial; that URL is not requested again. The article is `isOpenAccess: N` in Europe PMC but is held in PMC; the text and figures are stored under `files/fulltext/` (gitignored, shared, not committed): `PMC4653701_PMID26459563_pmc_html_2026-11-12.html` (sha256 cb96315bfc147075be418c0b423c1eb70d2c6bc42e4aef44af01c738f120cfea) and `PMC4653701_winkel2015_figures/` (nine JPEG files). Entry point A therefore stays as written. Prior S1 (full text reachable) holds in the form "reachable by the PMC page", not by the tool route.
