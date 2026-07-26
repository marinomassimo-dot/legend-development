# Independent structural red-team: the WWOX-Q230P "helix-lid / CMA degron" model

**Mandate.** Not "find a stabilizer" — *"tell me why this model might be wrong, and which experiment stops us from spending months on the wrong structure."* This dossier attacks the model. Where it survives, it survives having been attacked.

**One-line genotype class.** The worked example is a null/missense class: a canonical splice-acceptor allele is null-like (splice, NMD), so the **missense allele p.Gln230Pro** is the protein-making one. Everything in this red-team rides on Q230P.

**The model under test:**
> Q230P → destabilizes α-helix 226-251 → releases the lid packing against LRSVQ 187-191 → exposes a KFERQ degron → HSC70 → chaperone-mediated autophagy → lysosome → protein absent (= Johannsen).

---

## VERDICT: **WEAKENED** (structurally supported, mechanistically under-determined)

The model's **structural spine is sound** and, importantly, does *not* rest on a weak AlphaFold model — the SDR core is predicted at mean pLDDT 90.3 and the helix–degron geometry at inter-block PAE 1.4 Å, so the geometric claims can bear weight. But the **mechanistic half — that Q230P is degraded, by CMA, via the LRSVQ degron — is extrapolated, not measured**, and an equally-good alternative (global misfolding → quality-control degradation) explains *more* of the data. Three specific premises are false or unsupported. The model is not refuted; it is **not yet discriminated from its alternatives**, and it has borrowed certainty it hasn't earned.

Why not each other tag:
- **not SURVIVES** — premise 5 (LRSVQ) is weak, premise 8 (Q230P route) is untested, premises 9–10 are false; a model with a false link in its causal chain has not survived.
- **not REFUTED** — the core structural claims (helix real, lid packs on degron, anchors buried) held up under direct test; the disease-relevant *outcome* (protein absent) is measured fact. *(One structural sub-claim did fall — "C299R is catalytic" — see premise 11; that weakens a side branch, not the spine.)*
- **not INCONCLUSIVE** — we reached definite conclusions on 4 of the 11 premises and can rank the alternatives; the picture is not a shrug.

### Independent corroboration (second red-team, Codex 2026-07-13)
A separate analysis reached the same verdict class ("ridimensionato, non demolito") **independently**, converging on the same four weak points: Johannsen does not prove degradation, Zhang tests only P252A, LRSVQ is non-canonical while ERLIQ is canonical, and P252 lies outside the helix. Its structural numbers reproduce this report's to three decimals (C299↔H233 = 3.435 Å; DSSP α227-229 / π230-234 / α235-249). Two systems entering from different directions and failing on the same premises is the load-bearing signal. It also contributed **three refinements folded into this report**: (i) endosomal microautophagy (eMI) as a distinct alternative to CMA (M5, §3); (ii) the LAMP1-vs-LAMP2A distinction that leaves even P252A's route under-determined (§3, §5, missing-info 6); (iii) the L404-in-ERLIQ WWOX–GSK3β functional trap for any stabilizer (§5, §6, missing-info 7).

**A second audit (2026-07-14) then corrected four of my own numbers — all verified against the coordinates and accepted:** (1) **C299 is not catalytic** — my "3.4 Å from K297" was a backbone contact; the thiol SG–NZ distance is 10.7 Å, so C299R is a buried-core/lid destabilizer and the "two independent axes" claim is withdrawn (premise 11). (2) My **"+2.77 kcal/mol" was a helix-propensity scale value, not a folding ΔΔG** (≈ +1.5 kcal/mol is the honest ΔΔG); relabelled (premise 2). (3) The **KFERQ scan has 3 distinct loci, not 5 motifs** — three were overlapping frames of the C-terminal ERLIQ locus (§2). (4) The **fpocket run was on the whole protein**; re-run on the SDR alone, a real pocket (P12, 0.374) exists near the catalytic face, so "nothing near the triad / stabilizer infeasible" is withdrawn (§6). None of these four change the verdict — they remove over-reach and, if anything, make the model *less* clean (C299R may feed the same degradation route rather than a separate one).

---

## 1. Premises table with epistemic level

| # | Premise | Epistemic level | Red-team verdict |
|---|---------|-----------------|------------------|
| 1 | Q230P: transcript normal, protein absent (patient) | **Experimental** (Johannsen 2018) | **STANDS** — direct measurement |
| 1b | Johannsen resolved degradation vs. translation defect | *claimed* | **FALSE** — authors explicitly leave "impaired translation OR premature degradation" open |
| 2 | Q230 destabilizes helix 227-249 | Structural inference | **STRONG** — pLDDT 98.5; Q230→P helix-propensity penalty Δ +2.77 (Pace-Scholtz scale, *not* a folding ΔΔG — a proper ΔΔG estimate is ≈ +1.5 kcal/mol); Q230 sits in a π-helix bulge (locally strained) |
| 3 | Helix packs against LRSVQ anchors L187/V190 | Structural inference | **STRONG** — min. distances 3.4–3.5 Å, PAE 1.4 Å |
| 4 | The helix is a **lid** that buries the anchors | Structural inference | **MODERATE** — in-silico helix deletion exposes V190 (0→0.30) ≫ control; but static, no repacking, and L187 is co-buried by the ERLIQ segment |
| 5 | **LRSVQ is the operative KFERQ degron** | **Post-hoc hypothesis** | **WEAK** — LRSVQ is non-canonical (no acidic residue; needs pS189). ERLIQ 402-406 is a *better*, canonical motif |
| 6 | Exposed motif → HSC70 binding | Experimental (P252A only) | STANDS for P252A; **untested for Q230P** |
| 7 | HSC70 → CMA/lysosome → degradation | Experimental (P252A) | STANDS for P252A; extrapolated to Q230P |
| 8 | **Q230P uses the same CMA route as P252A** | **Extrapolation** | **UNTESTED — the single biggest gap** |
| 9 | Route is ubiquitin-independent | implied by "CMA not proteasome" | **FALSE / complicated** — Zhang shows P252A is strongly K63-polyubiquitinated |
| 10 | P252 caps/terminates the helix | Structural | **FALSE** — DSSP ends the helix at 249; P252 is in the following loop (rsa 0.42, exposed) |
| 11 | C299R acts via catalysis, not degradation | Structural inference | **RETRACTED / WEAK** — my "3.4 Å from K297" was a *backbone* N–C contact. The catalytic pair SG(C299)–NZ(K297) is **10.7 Å** (SG–Y293 12.8 Å, SG–S281 11.0 Å): C299's thiol is *not* near the catalytic machinery. C299 is a buried-core residue (packs L280/L397/I268) that also contacts lid-helix H233 at 3.44 Å ⟹ C299R is most likely a **destabilizer**, possibly feeding the *same* route as Q230P, not a separate catalytic axis |

*(full table: `premises_epistemic_table.csv`)*

---

## 2. The three specific things I falsified

1. **"LRSVQ is the degron."** A KFERQ scan of WWOX (canonical Dice rules) finds **3 distinct loci** — QGRDF 118 (canonical), LRSVQ 187 (phospho-dependent), ERLIQ 402 (canonical). *(An earlier draft reported "5 motifs"; three of those were overlapping reading frames of the single C-terminal ERLIQ locus and have been collapsed.)* LRSVQ 187-191 lacks the required acidic residue — it only qualifies if S189 is phosphorylated (never demonstrated). **ERLIQ 402-406 is fully canonical**, needs no modification, and its neighbours R408/L409 physically contact L187 in 3D. The model picked the weaker motif arbitrarily. *(`fig_kferq.png`, `kferq_scan.csv`)* **Double problem for the phospho-rescue:** S189 is not only un-phosphorylated in the curated record — in the folded model it is itself **helical and buried (RSA 0.12)**, so a kinase cannot even reach it in the native state. The phospho-activation of LRSVQ requires the protein to be unfolded first, which makes LRSVQ a *consequence* of destabilization, not the trigger the model needs.

2. **"P252 caps the helix."** DSSP places the helix at 227-249; **P252 is downstream in a loop** (SS = bend, RSA 0.42). It cannot be the C-cap. Its destabilizing effect, if real, is not via helix termination. *(`fig_helix.png`)*

3. **"Ubiquitin-independent CMA."** Zhang's own figures show P252A is **strongly K63-polyubiquitinated** (Ub-K63R reduces it). A clean "CMA-not-proteasome, therefore ubiquitin-independent" framing is contradicted by the source paper. K63 chains are a recognized route *into* selective autophagy — so this doesn't kill a lysosomal model, but it does kill the tidy dichotomy.

**And I falsified the team twice more, agreeing with your own retractions:** the "Q230 side-chain covers the motif" idea (Q230 is only the 5th-closest occluder) and "near KFERQ = severe" (C299R is buried, 19.6 Å from the motif). *Correction from a second audit:* I originally attributed C299R's severity to a catalytic lesion, citing "3.4 Å from K297" — but that was a backbone contact; the thiol is 10.7 Å from K297 and C299 is a buried-core/lid residue. C299R is therefore most likely another **destabilizer**, so the clean "two independent axes (degradation vs catalysis)" story does **not** hold. Proximity to the degron still does not predict severity — but the mechanism of the severe distant variant is destabilization, not catalysis.

---

## 3. Best alternative model

**M1 — global SDR misfolding → quality-control degradation (motif-agnostic).** Q230P (and P252A, L239R) destabilize the SDR fold; the exposed hydrophobic core is recognized by the chaperone/quality-control system (HSC70 among others), routed to the lysosome, with K63-polyubiquitin as a parallel/complementary tag. On the alternatives scorecard this fits **8/9 observations** — including the K63-polyubiquitination that the specific-degron model leaves unexplained — versus 7/9 for the original.

A close second, **M2**, keeps the entire helix-lid/CMA mechanism but replaces the degron with the canonical **ERLIQ 402-406**. M2 is important because it means *the model can be right in spirit and wrong in detail*: fixing the motif rescues it. *(`fig_falsification_matrix.png`, `alternatives_scorecard.csv`)*

**M5 — endosomal microautophagy (eMI), not CMA** *(added after an independent second red-team).* This is a distinct alternative the original scorecard did not separate, and it is not distinguished by *any* current data. eMI is also HSC70-dependent but routes through **ESCRT/VPS4 into late endosomes**, is **LAMP2A-independent**, and does not require a translocation-competent KFERQ. Two of Zhang's pillars fail to separate it from CMA: (i) chloroquine/NH₄Cl rescue blocks *all* lysosomal degradation, eMI included; (ii) HSC70 co-IP is shared by both routes. Critically, **Zhang shows colocalization with LAMP1 (a generic lysosomal marker), not LAMP2A (the CMA-specific receptor)** — so even for P252A the evidence is consistent with CMA *or* eMI *or* bulk lysosomal delivery. The "CMA" label is under-determined at its own source.

The decisive point: **every observation that currently supports CMA comes from P252A, is read out with LAMP1 not LAMP2A, and none tests Q230P.** The data do not uniquely select any of these models — and do not even pin the *route* within the lysosomal family.

---

## 4. Three new, prospective predictions

Each is a commitment the model makes that could fail:

1. **If M0/M2 is right:** Q230P protein is stabilized by chloroquine/NH₄Cl but **not** by MG-132, and co-IPs HSC70 — *just like P252A*. **If M1 is right:** the same rescue pattern holds, but a *second, unrelated* destabilizing SDR mutation (e.g. a buried-core Leu→Asp far from any KFERQ motif) shows identical HSC70/lysosome behaviour — degradation tracks fold stability, not motif identity.
2. **Degron epistasis:** introducing **Q406A** (ERLIQ Gln) in cis with Q230P restores protein level more than **Q191A** (LRSVQ Gln) does — because ERLIQ is the canonical, exposed motif. (M0 predicts the opposite ranking.)
3. **C299R route test (revised):** because C299 is now assessed as a **buried-core/lid destabilizer** (SG 10.7 Å from K297, contacts lid H233), the model predicts C299R behaves like Q230P — degraded and **chloroquine-rescued**. If instead C299R is *not* CQ-rescued, that would restore a distinct (e.g. catalytic or aggregation) route. Either way this now tests whether "distant severe variants converge on the degradation route," not a catalysis-vs-degradation split.

---

## 5. Priority discriminating experiment

**A cycloheximide-chase degradation panel with degron epistasis in cis** (full protocol: `discriminating_experiment.md`). Six arms — WT, **Q230P**, Q230P+Q191A, Q230P+Q406A, P252A (positive control), C299R (route control) — each read under CHX chase, **chloroquine/NH₄Cl (primary probe)**, MG-132 (specificity control), and HSC70 knockdown.

Two design points that are the whole value of this red-team:

- **MG-132 must NOT be the primary readout.** In the nearest analog it is mute on WWOX. A team defaulting to it would see no rescue, conclude "degradation isn't the bottleneck," and kill the best hypothesis with a false negative. **CQ/NH₄Cl is the readout; MG-132 is the control.** Cost of getting this right: two wells.
- **Knock out the degron at the essential glutamine, not the hydrophobic anchors.** L187A/V190A are fully buried (RSA ≈ 0) — mutating them destabilizes the fold itself, so any drop in protein is uninterpretable. **Q191 (RSA 0.28) and Q406 (RSA 0.58) are exposed**, carry little structural load, and Q is the non-substitutable KFERQ residue. This is the clean knockout, and it closes the hole in Zhang (the motif was never mutated).

Every cell of the outcome matrix maps to a specific model verdict — including a "Q230P is not degraded at all" arm that would refute the whole degradation framing in favour of a translation/folding-yield defect (M4).

**Two additions adopted from the second red-team** (they sharpen the same experiment rather than replacing it):
- **Separate CMA from eMI, don't just confirm "lysosome."** Add a **LAMP2A knockdown** arm (blocks CMA, spares eMI) alongside a **VPS4/ESCRT block** arm (blocks eMI, spares CMA). Rescue by LAMP2A-KD ⟹ CMA; rescue by VPS4 block ⟹ eMI (M5); rescue by neither but by chloroquine ⟹ bulk lysosomal. This is the missing distinction — chloroquine alone cannot make it.
- **Read function, not just abundance, in the same experiment.** Because the canonical degron ERLIQ 402-406 *contains L404*, a residue implicated in the WWOX–GSK3β interaction, measure a functional output (GSK3β/Tau readout) in parallel with protein level. This pre-empts the "stable-but-inert" failure mode before any stabilizer exists: if the Q406A/ERLIQ arm restores abundance but loses GSK3β function, an interface stabilizer there is a NO-GO by construction.

---

## 6. Conditional druggability map (gated on the model surviving)

*Only meaningful if the experiment confirms Q230P is degraded via a stabilization-sensitive route.* **Corrected after a second audit:** my first pass ran fpocket on the *whole* protein (WW domains + disordered N-terminus included) and over-concluded. Re-running on the **SDR domain alone (125-414)** gives the honest map. *(`fig_druggability.png`, `pocket_analysis_SDRonly.csv`, `pocket_analysis.csv`)*

**A druggable pocket does exist on the SDR — but not at the degron interface.** The best SDR pocket (**P12, druggability 0.374**) is lined by residues 215-218 / 287-290 / 334-338 and sits **10.7 Å from the catalytic triad**, near the catalytic face — *not* at the helix-degron interface. At the **helix–degron interface specifically there is still no druggable pocket** (nearest, P2 = 0.004). So the two things I over-claimed are withdrawn: it is **not** true that "there is nothing to bind near the triad," and it is **not** established that a stabilizer is "infeasible." What holds is narrower: **the interface you'd want to stabilize (helix-lid on degron) is not itself a pocket**, while the only real pocket is close enough to the catalytic face (10.7 Å) that triad occlusion becomes a genuine selectivity concern rather than a non-issue.

**A second functional exclusion zone, beyond the triad** *(added after the second red-team).* The catalytic triad is not the only region a stabilizer must avoid. The canonical degron **ERLIQ 402-406 contains L404, implicated in WWOX–GSK3β binding** (L404 is buried, RSA 0.02, structurally embedded in the same segment). Any ligand that stabilizes WWOX by clamping the ERLIQ region therefore risks **rescuing abundance while abolishing the GSK3β/Tau function** — the textbook "stable-but-inert" NO-GO. So the permissive-stabilizer profile you defined (`Q230P↑ + half-life↑ + HSC70/LAMP1↓ + SDR function preserved`) must be extended: **preserve GSK3β binding too.** This narrows an already-empty pocket landscape further — the two candidate degron regions each abut a function that must not be touched (LRSVQ near the mito/MAPT region, ERLIQ containing L404).

Realistic routes, in order of risk:
- **Target the route, not the protein** (lowest risk, least selective): HSC70/HSPA8 modulation or lysosomal inhibition — but non-selective, and only after CMA is confirmed. Note a hazard flagged in your own dossier: HSC70 *delivers* substrates to the lysosome, so an HSC70 activator (e.g. arimoclomol-like) would likely *worsen* degradation — the sign of the effect must be established before any chaperone is chosen.
- **Cryptic-pocket / molecular-glue campaign** (high risk, high leverage): a stabilizer would need a pocket absent from the static WT fold, or an interface glue — both require the experimental SDR structure that does not yet exist.

---

## 7. Principal failure modes (how *this red-team* could be wrong)

1. **AlphaFold is not a crystal structure.** All burial, packing, and pocket claims rest on one model. It's high-confidence (pLDDT 90.3, PAE 1.4 Å) and internally consistent, but a single unmodelled conformational state (e.g. an open/closed SDR) could change the lid and pocket picture entirely. **The 20-year hole — no experimental SDR structure — is the real bottleneck, and everything here inherits that uncertainty.**
2. **The lid-removal test is static.** Deleting the helix without repacking gives *upper bounds* on exposure; the V190-vs-control contrast is the real signal, not the absolute numbers.
3. **Motif scan uses a rule-based definition.** KFERQ-finder rules are heuristic; a non-canonical motif can still be a real CMA signal, and a canonical one need not be used in vivo. The scan reorders the *priors*, it doesn't settle biology.
4. **M1 vs M2 vs M0 is my ranking, not a measurement.** The scorecard weights observations equally; a different weighting could reorder them. That is exactly why the discriminating experiment matters.

---

## 8. Missing information (what would move the verdict most)

1. **Any degradation assay on Q230P itself** — CHX half-life, HSC70 co-IP, LAMP1 colocalization, CQ vs MG-132 rescue. This single dataset would move the verdict off WEAKENED in either direction. *(Currently the entire mechanism is P252A-derived.)*
2. **An experimental structure of the WWOX SDR domain** (crystal or cryo-EM). The only PDB entry, 1WMV, is the 54-residue WW2 domain — not the SDR, not Q230's domain.
3. **Whether S189 is phosphorylated in vivo** — determines if LRSVQ can be a degron at all (and note S189 is buried in the fold, so this can only happen post-unfolding).
4. **The half-life of Q230P vs. WT** at endogenous level in patient (Gln230) fibroblasts — Aqeilan/Johannsen have the lines.
5. **Whether K63-polyubiquitination is required for the lysosomal route** (Ub-K63R + CQ epistasis) — resolves premise 9.
6. **CMA vs eMI: LAMP2A-dependence of the route** — a LAMP2A knockdown / VPS4 block that Zhang's LAMP1 colocalization cannot settle. Determines whether "CMA" is even the right label.
7. **Residue-level confirmation that L404 is required for WWOX–GSK3β binding** — cited (Wang et al., PMC3354054) but not verified here; it sets whether the ERLIQ region is a functional no-touch zone for a stabilizer.

---

### Bottom line for the team
The lid geometry is real and the AlphaFold model is good enough to reason on — you were right not to trust the crystal-structure-shaped hole to stop you. But the causal chain has a soft middle: **you have inferred Q230P's fate from a cousin variant, chosen the weaker of two degron motifs, and inherited a ubiquitin-independence claim your source paper contradicts.** One two-week Western-blot panel — with chloroquine as the readout instead of MG-132, and the glutamine mutated instead of the buried anchors — tells you whether the SDR structure is worth chasing. Do that before the medicinal chemistry, because the druggability map says the chemistry is the hard part: there is no pocket waiting for you at the interface.
