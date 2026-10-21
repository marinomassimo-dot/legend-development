# Repurposing precedents and the design of an early-benefit evaluation - group R4

> **Actor** `scientist-d` - **Task** `REPURP-10H-R4-D-20261021` - 2026-10-21. Non-canonical research record: it touches none of the four scientific current files, `disease_model.md`, `drug_repurposing/` or `repurposing_bridge.py`.
>
> **NOT WWOX EVIDENCE, at class level, for every paper below.** Each is a trial, protocol, natural-history study or review in another disease (TSC, CDKL5, Dravet, Lennox-Gastaut, STXBP1, SCN2A, GRIN1/GRIN2B, synaptic disorders). Trial designs and regimens appear only as **design facts of a published study**, never as guidance: no dose, no administration recommendation, no paediatric suitability presumed for anything. Nothing here is medical advice; it supports discussion with a treating clinical team and never substitutes for one.
>
> **Context policy** `QUESTION_DRIVEN` (the early-benefit note and the known-roads note were read first and are held). Locators were captured while each document was open; the registry comparison (`registry_records.py get --pmid <PMID> --hops 1`) was run after each first pass and returned NO RECORD for every paper so far; that is a statement about the query, not about what the laboratory knows.
>
> **Two repository facts every extraction is set against.** (1) In the only WOREE series reporting any therapeutic response the developmental-delay row is identical in all columns, diet responders included, and two of the three responders had died (PMID 36537114, blind-audited 2026-10-21). (2) No pharmacodynamic readout for WWOX exists: the three direct read-outs have no limit of detection, linear range or calibrator (CLAIM 046).

The question put to each paper: **what would an evaluation of a repurposed drug in WOREE have to measure, and what would it not be able to claim?**

---

## Per-paper readings

### 33180985 - Kotulska 2021, EPISTOP (tuberous sclerosis, pre-symptomatic antiseizure treatment) - NOT WWOX EVIDENCE

Receipt `FTR-20261021-33180985-01` (complete, staged) - manifest PASS, 19 locators (17 body, 2 figure attestations). Figures 1 and 2 opened as page renders after `paper_packet.py rank` flagged the Figure 2 page as likely vector.

- **Design (DATO).** Infants with definite TSC and no seizure history, video-EEG monthly; a drug was started either at first epileptiform EEG activity (preventive) or after the first seizure (conventional). Randomised at 6 sites (13 versus 14); at 4 sites ethics boards refused randomisation, so a parallel **non-randomised open-label** group was enrolled (12 versus 15). Caregivers and treating physicians were blinded to the EEG data; EEG readers and psychologists blinded to allocation.
- **Endpoint type.** Primary: **time from birth to first clinical seizure** (event-time count outcome). Secondary at 24 months: drug-resistant epilepsy, infantile spasms, diary-derived proportion of days with seizures (count-derived), and **instrument endpoints** Bayley-III cognitive score below 70 and ADOS-2.
- **Symptomatic versus modifying.** Not separated. The "modification" claim is a seizure-endpoint claim ("natural history of seizures"). The instrument endpoint (neurodevelopmental delay) was **not significantly different** (RCT 33% versus 50%; text and Table 3 disagree on the open-label figures, 20/30% in text, 17/25% in Table 3). The authors give three reasons (small n, follow-up to 2 years, benefit of intensive monitoring in the control arm) and add that processes before the surrogate-triggered start may already shape outcome.
- **Control.** Conventional (post-seizure) treatment; randomised in half the infants only. **Both arms received the surveillance**, so the contrast is timing of the drug, not drug versus nothing; the authors name two interventions bundled in the strategy.
- **Conditioning.** Infants with a seizure before the EEG trigger (22 of 94) were excluded from the primary and secondary analyses; the analysed set is conditional on the surrogate appearing first. The abstract's medians (364 versus 124 days) are for patients **who developed seizures**.
- **Statistical fragility visible in the tables (DATO).** In the randomised part alone, clinical seizures at 24 months p 0.202, infantile spasms p 0.096; drug-resistant epilepsy p 0.047; significance of several headline results comes from **pooling randomised and non-randomised** infants. Text reports p 0.011 for the randomised seizure-free proportions but the randomised panel of Figure 2 prints log-rank p 0.009 and the 0.011 sits on the open-label panel (panel versus text, recorded as two entries). Table 2 prints a pooled median age "9996" (typographical artefact, not interpreted).
- **Follow-up.** 24 months; no effect on development at that time; a pilot's school-age follow-up is cited by the authors, not read here.
- **What it gives a card.** A surrogate-triggered pre-symptomatic start needs a **validated trigger**; WOREE has none (no qEEG, no fluid marker, no pharmacodynamic readout). A seizure-time endpoint can look significant while the developmental instrument does not move: the same dissociation the WOREE diet series prints.
- **What it cannot claim.** Disease modification of development. Class-level inference only; no transfer of any regimen.

