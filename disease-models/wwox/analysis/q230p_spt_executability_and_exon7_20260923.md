# `Q230P` — is the S/P/T experiment ACTUALLY EXECUTABLE? · and is the exon-7 RNA question cheap?

**Actor:** SCIENTIST-A · **Date:** 2026-09-23 · **Type:** BOUNDED EXECUTABILITY AUDIT — not a discovery wave
**Status:** NON-CANONICAL. No `*_current.md`, no registry, no queue, no ledger, no receipt, no state
manifest, no Operator-gated commit candidate and no discovery-method V0 file was modified. No
`BATCH_COMMIT`. No `git` command that writes. No purchase, no quotation, no external contact.
**Nothing here is medical advice.** No molecule, dose, route or clinical framing appears.
**Public edition.** Reference WWOX-DEE genotype class only — no individual, no pedigree coordinate,
no parent-of-origin, no re-identifying variant combination.

> **What this file is.** Yesterday's read of Johannsen 2018 ended by naming one experiment
> ([`johannsen2018_fulltext_q230p_revival_20260923.md:320`](johannsen2018_fulltext_q230p_revival_20260923.md)):
> *"One denaturing-resolubilised S/P/T blot on `Q230P` fibroblasts, with a dilution-series LOD and
> **two epitope-flanking antibodies**."* This file asks one question about it — **can it be bought
> and run, reagent by reagent** — and one question beside it: **is the exon-7 RNA discriminator cheap?**
> 🔴 It does **not** re-argue whether the experiment is worth doing. That was settled elsewhere.

---

## 0 · Instrument check, run first and recorded whatever it said

`DATO` — executed 2026-09-23, this deployment, verbatim terminal result:

```
curl https://www.scbt.com/...        → curl: (56) CONNECT tunnel failed, response 403
curl https://www.ptglab.com/...      → curl: (56) CONNECT tunnel failed, response 403
curl https://www.sigmaaldrich.com/...→ curl: (56) CONNECT tunnel failed, response 403
curl https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_016373
                                     → connect_rejected (egress proxy denied CONNECT)
curl https://rest.ensembl.org · https://www.ebi.ac.uk/proteins · https://api.genome.ucsc.edu
                                     → 403, 403, 403
```

🔴 **Three consequences, declared before any reagent is discussed.**
1. **Every vendor listing status in this file is `UNKNOWN — VENDOR DATASHEET BLOCKED`.** Not
   *"probably still sold"*, not *"discontinued"*. The census's rule stands
   ([`wwox_antibody_epitope_census_20260922.md:108`](wwox_antibody_epitope_census_20260922.md)):
   *"A catalogue number is **not** an epitope."* It is also not a stock level.
2. **No reference sequence is reachable.** `NM_016373` cannot be fetched here, and no FASTA, GenBank
   or transcript file exists anywhere in this repository (`find` over the whole tree: zero hits).
   Every primer-position statement in §5 is therefore either **arithmetic on facts the papers
   themselves print**, or **`UNKNOWN`**. 🔴 **No sequence was reconstructed from memory.**
3. The **Methods channel is open while the datasheet channel is shut** — the census's own §5.1
   finding. §1.1 below is what that channel returned when asked one bounded question.

---

# TASK 1 · REAGENT REALITY AUDIT

## 1.1 🎯 The finding that reorganises the audit: **`A17` and `A21` are ONE antibody, and it is `sc-20528`**

One bounded retrieval was run (`"sc-20528"` on PubMed → **0 records**, an instrument reading, not a
finding; then one Scholar Gateway passage query). It returned the **Materials and Methods of
Suzuki 2009** — the *lde* rat paper the census carries as row **`A17`, antibody "unnamed"**
([`wwox_antibody_epitope_census_20260922.md:135`](wwox_antibody_epitope_census_20260922.md)):

> `DATO`, verbatim, Suzuki H *et al.* 2009, *Genes Brain Behav* 8(7):650–660,
> [DOI 10.1111/j.1601-183X.2009.00502.x](https://doi.org/10.1111/j.1601-183X.2009.00502.x),
> Materials and methods (retrieved by Scholar Gateway, publisher passage body, 2026-09-23; the text
> layer deletes hyphens and superscripts — characters otherwise unaltered):
>
> *"the membranes were incubated with **goat antiWwox polyclonal antibody (1:100; sc20528, Santa
> Cruz Biotechnology**, Santa Cruz, CA, USA) and mouse antiactin monoclonal antibody …, followed by
> incubation with **Alexa Fluor 680 conjugated rabbit antigoat** immunoglobulin G (IgG) antibody
> (1:20 000; Invitrogen) and IRDye 800 conjugated donkey antimouse IgG antibody … Signal intensities
> were quantified using the **Odyssey infrared imaging system** … **The Wwox epitope bound by the
> antiWwox antibody used in this study did not contain the region altered by the lde mutation
> (personal communication from Santa Cruz Biotechnology).**"*

`INFERENZA` (identity): the catalogue number, the vendor, the host and the anti-goat secondary all
match `A21` exactly. **`A17` ≡ `A21` ≡ `sc-20528`.** Four things follow, and each is separated from
the others deliberately:

| # | | Tag |
|---|---|---|
| **1** | **The founding `Q230P` blot and the founding *lde*-rat blot were read through the same catalogue antibody.** Johannsen 2018 at 1:200 on human fibroblasts; Suzuki 2009 at 1:100 on rat testis and hippocampus | `INFERENZA` from two verbatim Methods |
| **2** | **`sc-20528` is `goat`, polyclonal — now `DATO`, not inference.** The census marked the host 🟡 *"entailed by the paper's own secondary"* (`:140`). Suzuki prints it directly | `DATO` |
| **3** | **`sc-20528` has an epitope statement after all — a NEGATION, vendor-sourced by personal communication in 2009, with no residue range.** It does not contain the region altered by `p.Leu371Thrfs*53`, i.e. roughly the last ~44 residues. 🔴 **This excludes the extreme C-terminus and NOTHING ELSE. It does not place the epitope relative to residue 230.** The sibling sentence the census already held — *"does not recognize the C-terminal amino acid sequence"* (`:135`) — is the same statement, and its provenance is now known to be **a phone call to a vendor**, not a datasheet and not an experiment | `DATO` + `INFERENZA` on scope |
| **4** | 🔴 **The antibody that produced `Q230P`'s founding negative is the antibody with a documented, in-print false negative.** Census §4.1 rows 2→3 (`:268`–`:269`): with this reagent, *"both products were **undetectable**"*; ten years later, in the same rat model, with `HPA050992`, *"a **very weak band of slightly lower mobility** was detected"* | `INFERENZA`, drawn from two published results the census already holds |

🔴 **How far point 4 may be pushed, and no further.** Suzuki's buffer is a real RIPA
(*"150 mM NaCl, 10 mM TrisCl (pH 8.0), 0.1% SDS, 1% TritonX100, 1% sodium deoxycholate, 5 mM EDTA"*)
and Tochigi's is also a real RIPA with sonication — so the two runs are **not** separated by lysis
class. But **three** variables still differ: the antibody, **sonication** (Tochigi sonicates, Suzuki
homogenises only) and **detection** (ECL/`ImageQuant` vs Odyssey IR in Suzuki — note Suzuki's own
detection was IR, the *more* sensitive of the two). The Tochigi authors attribute the difference to
the antibody, *"may have been due to greater sensitivity of the new antibody"* — **an author
attribution, tested by nobody.** `IPOTESI`, not `DATO`: *`sc-20528` is the less sensitive reagent.*
**It is unproven, it is cheap to test, and §3 tests it for free by running both antibodies on the
same membrane.**

> 🔴 **Owed to the census, not applied here** (this file edits no other file): `A17` and `A21` are
> one row. Distinct anti-WWOX primaries **18 → 17**; *"no epitope information of any kind"*
> **10/18 → 9/17**; the *"epitope stated only as a negation"* class now contains the **founding
> `Q230P` antibody**. 🟢 **The zero is untouched: still 0 wholly C-terminal to 230.**

## 1.2 The audit table — eight fields, each stated separately

**Rule applied throughout, and it is the point of the exercise:** *presence in the census is not
availability.* `ORDERABLE` means **a vendor + a catalogue number a purchasing office could type**.
It does **not** mean the item is in stock, current, or that its datasheet says what one hopes.

| Row | Exact identity (vendor · catalogue · clone) | Epitope / immunogen **as STATED** | Human reactivity | WB-validated? | Expected MW behaviour | Commercial / historical / unknown | Denaturing SDS-urea WB compatible? | Side of residue 230 |
|---|---|---|---|---|---|---|---|---|
| **A1** 🥇 | **Sigma-Aldrich · `HPA050992`** · rabbit polyclonal, PrEST class · no clone (polyclonal) | 🟢 **STATED by residue range:** *"directed against **amino acids 32–110 of human Wwox protein**, a sequence **100% identical** to that of rat Wwox"* (`census:119`) | 🟡 **By immunogen, yes — the immunogen IS human WWOX.** 🔴 **But every WB attested in a source read by this repository is on RAT tissue.** No human-lysate WB of `HPA050992` has been read first-hand here → `UNKNOWN in practice` | 🟢 WB 1:1000 (+ IHC-P, IF). 🔴 **Not** KO-validated, **not** peptide-blocked; its negative control is biological (no normal-mobility band in `lde/lde`) | Detects WWOX at **46 kDa**; detected the `lde` frameshift product at **46.2 kDa**, *"theoretically 0.8 kDa larger than wild type"* ⇒ 🟢 **it resolves ~0.8 kDa on a standard gel** | 🟡 **Catalogue number attested in a 2019 Methods section.** Listing status 2026: **`UNKNOWN — VENDOR DATASHEET BLOCKED`** (`RT-AB-04`, census `:358`) | 🟢 **Yes** — used on a DOC+SDS RIPA lysate, sonicated, SDS-PAGE | 🟢 **WHOLLY N-TERMINAL.** Ends **120 residues** before Q230 |
| **A21 = A17** | **Santa Cruz Biotechnology · `sc-20528`** (printed `sc20,528` by Johannsen's typesetter) · **goat** polyclonal · no clone | 🟡 **STATED ONLY AS A NEGATION:** *"The Wwox epitope … **did not contain the region altered by the lde mutation** (personal communication from Santa Cruz Biotechnology)"*. 🔴 **No residue range, no immunogen, no peptide. Provenance = a vendor phone call, 2009** | 🟢 **YES, first-hand and strong:** human dermal fibroblasts, HEK293, PaTu-8988t, SW620 (Johannsen `:213`); also rat (Suzuki). **Cross-reactive human + rat** | 🟢 **The best-controlled specificity in the census:** three CRISPR/Cas9 `WWOX` **knock-out** PaTu-8988t clones as a true negative + three positive lines (`census:140`). 🔴 **Zero sensitivity validation** — no dilution series, no standard, no LOD | Band at **~46 kDa** (Johannsen); in rat, *"products"* at the same class of mass | 🔴 **`UNKNOWN — VENDOR DATASHEET BLOCKED`.** It was a live catalogue item in 2009 and was still citable in 2018. **Whether Santa Cruz lists it in 2026 could NOT be determined here and is NOT guessed** | 🟢 **Yes** — 12% SDS-PAGE, reducing sample buffer, 94–95 °C, in **both** papers | 🔴 **UNRESOLVED.** Excludes only ≈aa 371–414. **Could be either side of 230** |
| **A6** | **Abcam · 🔴 CATALOGUE NUMBER NOT GIVEN** | 🟢 STATED by exon range: *"a peptide translated from **exons 1–5**"* ⇒ aa 1–172 (`census:124`) | 🟢 Human fibroblasts | 🟢 Isoform-discriminating on the same blot as A5 | Resolves the **46 kDa long isoform** from the **WW-only short isoform** | 🔴 **NOT ORDERABLE. A supplier name is not a catalogue number, and an antibody you cannot order is not a reagent.** Abcam lists hundreds of anti-WWOX SKUs; nothing in the source selects one | Presumed (SDS-PAGE WB) — not separately stated | 🟢 N-terminal, stops **58 residues** before 230 |
| **A5** | **ProteinTech · 🔴 CATALOGUE NUMBER NOT GIVEN** | 🟢 STATED by exon range: *"exons 1–7"* ⇒ aa 1–≈280 (`census:123`) | 🟢 Human fibroblasts | 🟢 Same blot as A6 | Same isoform pair | 🔴 **NOT ORDERABLE — same failure.** 🔴 And note the second defect: its C-terminal reach is **`±30 aa`** because the repository's own exon 7/8 boundary is bracketed, not fixed (`RT-AB-03`, census `:357`) | Presumed | 🔴 **SPANS 230** — and *"spans"* is not *"flanks"*: a spanning immunogen tells you nothing about which fragment you are seeing |
| **A2** | **Aldaz lab, MD Anderson · 🔴 IN-HOUSE, NO CATALOGUE** | 🟢 STATED twice (`≈16–93` / `12–94`) **and mapped empirically**: *"preadsorption … to a GST fusion protein containing the **WWOX WW domains** completely eliminated immunohistochemical reactivity"* (`census:120`) | 🟢 human + mouse conserved | 🟢 **The only strictly KO-validated reagent in the census**, plus a competition control | 46 kDa class | 🔴 **NOT ORDERABLE. `HUMAN_REQUIRED`: an author request and an MTA.** Best-characterised reagent in the field and not purchasable by anyone | Presumed | 🟢 N-terminal, fixed **twice** |
| **A3** | Huebner/Croce lineage · **Cocalico Biologicals custom · 🔴 NO CATALOGUE** | 🟢 Immunogen = **full-length WWOX aa 1–414** (GST fusion) | 🟢 human | 🟢 titred against `WWOX`-deleted cells; IHC blocked by cleaved Wwox | 46 kDa class | 🔴 **NOT ORDERABLE — a custom antiserum from 2004.** Bleeds are finite | Presumed | 🔴 **SPANS 230, epitope within the immunogen UNMAPPED** |
| **A7 · A8 · A9 · A10 · A13** | 🟢 **Orderable numbers:** Abcam `ab238144`, Abcam `ab189410`, Merck Millipore `ABN413`, CST `4045S`, Abcam `ab216660` | 🔴 **UNSTATED, all five.** Every route is a datasheet; every datasheet returned **403** today (§0) | A7/A10 human WB context; A8 human IHC; A9/A13 unattested for any WWOX result | 🔴 **None published.** A9 is the reagent that was **bought and never reported** (blocker `B6`); A13 is `catalogue-listing` only | UNKNOWN | 🟢 **ORDERABLE — and this is the only field in which they beat A5/A6** | UNKNOWN | 🔴 **UNKNOWN — this is blocker `B7`, and it is what makes the flanking pair impossible** |
| **A11 · A12** | Abcam `ab193624` · `ab129881` — **anti-WWOX phospho-Y33** | 🟡 modification site `Y33` only | — | — | — | 🟢 orderable | — | 🟢 N-terminal 🔴 **but phospho-restricted: they measure a modification, never abundance. Structurally unusable here** |
| **A4 · A14 · A15 · A16** | 🔴 in-house / citation-only; `A14`'s authors themselves print `Catolog No **N.A**` | 🔴 UNSTATED | — | partial | — | 🔴 **NOT ORDERABLE** | — | 🔴 UNKNOWN |
| **A18 · A19** | Sigma `F1804` (FLAG M2) · anti-myc | 🟢 the **tag**, not WWOX | n/a | n/a | tag-dependent | 🟢 orderable | 🟢 | 🔴 **Requires a transfected construct ⇒ cannot be used on patient fibroblasts at all** |
| **A20** | anti-C-DmWWOX | *Drosophila* | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ **OUT OF SCOPE** |

## 1.3 The audit's answer, in one block

| Question | Answer |
|---|---|
| Anti-WWOX antibodies **orderable by catalogue number** | **7** — `HPA050992`, `sc-20528`, `ab238144`, `ab189410`, `ABN413`, `4045S`, `ab216660` (+ the two phospho and the two tags) |
| Of those, **with any epitope statement at all** | **2** — `HPA050992` (residue range) and `sc-20528` (a negation) |
| Of those, with an epitope **placed relative to residue 230** | 🟢 **1. `HPA050992`, and it is N-terminal.** |
| **Wholly C-terminal to 230, orderable or not** | 🔴 **0. Unchanged by everything found today.** |
| 🔴 **`A5` and `A6` — the two antibodies yesterday's §6 named for the blot** | 🔴 **NEITHER IS A REAGENT. Both carry a supplier name and no catalogue number** (`census:123`, `:124`). **They cannot be written into a protocol, cannot be quoted by a purchasing office, and cannot be ordered.** Recovering them is author correspondence — `HUMAN_REQUIRED`, census §6.4 item (iv) |
| Is `sc-20528` still a current Santa Cruz item? | 🔴 **`UNKNOWN — VENDOR DATASHEET BLOCKED`** (§0). **Not guessed.** If it is discontinued, the one reagent that makes a new result commensurable with the founding negative is gone, and §3 loses its second channel |
| Is `HPA050992` still listed? | 🔴 **`UNKNOWN — VENDOR DATASHEET BLOCKED`.** `RT-AB-04` was raised on 2026-09-22 and is **still open**: *"One human, one browser, ten minutes."* |
| A **quantified recombinant human WWOX standard** for an LOD in ng | 🔴 **`UNKNOWN`.** None is named in any source this repository has read; the minimum discriminator states *"no purified folded WWOX SDR exists"* (`q230p_minimum_discriminator_20260922.md:246`). Whether a catalogue full-length recombinant exists is a **vendor question** and is blocked |

> 🎯 **One executability fact that nobody asked for and that changes the design.**
> `HPA050992` is **rabbit**; `sc-20528` is **goat**. Two hosts ⇒ **two secondaries in two channels on
> ONE membrane** — and Suzuki 2009 has already published the exact pairing (*"Alexa Fluor 680
> conjugated rabbit antigoat"*, Odyssey two-colour). `INFERENZA`: **the two-antibody read is not two
> blots and involves no stripping.** It is the same lanes, imaged twice, with no re-probing
> artefact. That is a real cost reduction and it is available today.

---

# TASK 2 · CLASSIFICATION OF THE S/P/T EXPERIMENT

> ## 🟡 **`MINOR ADAPTATION`**

**Not `EXECUTABLE NOW`**, and the reason is specific rather than general: the experiment as written
in [`johannsen2018_fulltext_q230p_revival_20260923.md:320`](johannsen2018_fulltext_q230p_revival_20260923.md)
and [`q230p_minimum_discriminator_20260922.md` §3.1](q230p_minimum_discriminator_20260922.md)
specifies **"two epitope-flanking antibodies"** and names `A5` + `A6` as the reagents. 🔴 **Those two
antibodies have no catalogue numbers, and the flanking pair does not exist in any form.** A protocol
cannot be executed against a supplier name.

**Not `NEW REAGENT`** either, and this is the more important half of the verdict: **nothing has to be
raised, cloned or invented.** Every adaptation below is a substitution among things that already
exist, or a technique change.

| # | Adaptation required | Cost | Why it is minor |
|---|---|---|---|
| **M1** | **Replace the flanking pair with `HPA050992` (aa 32–110) + `sc-20528`** and score **band size** as the primary discriminator, not signal | 🟢 zero — both are catalogue items | One membrane, two hosts, two IR channels (§1.3) |
| **M2** | Verify both are still listed | 🔴 `HUMAN_REQUIRED` — ten minutes, one browser | Blocked here, trivial there. 🔴 **If `sc-20528` is discontinued the design falls back to one antibody; §3 states what is lost** |
| **M3** | **The C-terminal read becomes a bench measurement, not a purchase:** fragment competition against the GST fusions `ww (1–110)` and `ADH (110–414)`, already defined verbatim in PMID 22193544 | 🟢 *"two bacterial preps, two blots, one afternoon"* (census `:215`, substitute **S2**) | Converts an unreachable datasheet into a measured fact. It also **maps `sc-20528` itself**, which is the single most valuable unknown in the whole file |
| **M4** | **LOD reported in cell-equivalents, not ng**, unless a quantified standard is sourced | 🟡 a declared downgrade | A ≥5-point dilution series of a **control fibroblast lysate** on the same membrane is fully executable today and converts *"absent"* into *"below the signal of X % of one control-cell-equivalent, N = 3"*. 🔴 That is **not** the ng figure `DET-4` asked for, and the file says so rather than renaming it |
| **M5** | **Do not boil urea samples.** If `P` is resolubilised in 8 M urea, heat ≤ 50 °C (carbamylation); if the protocol wants 95 °C, use 2 % SDS without urea | 🟢 zero | 🔴 `q230p_minimum_discriminator_20260922.md` §3.1 specifies *"95 °C"* for a **SDS/urea** buffer. That is a real bench error in the written protocol and it is corrected here, not inherited |
| **M6** | **A human WWOX-null lane.** Johannsen's three CRISPR KO clones are **PaTu-8988t, in the authors' freezer** — not orderable. Substitute: siRNA/shRNA knockdown in a control fibroblast (the `sc-403070` plasmid class is catalogue) | 🟡 weeks, standard | 🔴 A knockdown is not a null; the lane is then *"strongly reduced"*, not *"absent"*. **Declared, not smoothed** |
| **M7** | 🔴 **`Q230P` fibroblasts** | 🔴 **`HUMAN_REQUIRED`, and it is the binding constraint** | **This is a material problem, not a reagent problem**, and it was already `HUMAN_REQUIRED` before today (`q230p_minimum_discriminator_20260922.md` §3.2, *"the binding cost is not money or time: it is material access"*). It is outside this audit's scope and is **not** what moves the verdict from `EXECUTABLE NOW` |

🔴 **Justification against enthusiasm, stated plainly.** Yesterday's §6 wrote *"every reagent is
already identified in files this repository holds."* **That sentence is true and misleading.** Two
of the three antibodies it named are **identified and unbuyable**. The experiment survives — but it
survives by changing its reagent list, and the version of the design that says *"flanking pair"*
should not be quoted again without the correction in §1.3.

---

# TASK 3 · THE COMPRESSED EXPERIMENT

> ## ONE QUESTION ONLY:
> ## **Is WWOX/`Q230P` signal absent from the ENTIRE RECOVERABLE CELLULAR PROTEIN POOL, or only from the soluble fraction Johannsen assayed?**

Everything that does not serve that question is cut: no inhibitors, no 30 °C, no chase, no
localisation, no transgene arm, no qPCR (it moves to §5 as its own micro-experiment), no compound.

### 3.1 Fractions — three, from paired wells, at equal cell-equivalents

| Lane class | Preparation | Why exactly this |
|---|---|---|
| **`S`** | 🎯 **Johannsen reproduced verbatim:** *"resuspended in 100 μl ice-cold **RIPA** buffer supplemented with protease inhibitors and **sonicated three times on ice**. Upon **10 min centrifugation with 13.000 rpm at 4 °C**, the supernatant containing cellular proteins was collected"* (`johannsen2018…:58`) | 🔴 **The composition of his RIPA is UNSTATED and unrecoverable** (`P2`). **Therefore `S` must be run with a stated recipe of the DOC+SDS class and the substitution declared** — Suzuki 2009's own RIPA (`0.1 % SDS, 1 % Triton X-100, 1 % sodium deoxycholate, 150 mM NaCl, 10 mM Tris pH 8.0, 5 mM EDTA`) is the nearest published WWOX-specific recipe and is quoted in §1.1. 🔴 **A negative in `S` is then commensurable with Johannsen's *by class*, never *by identity*** |
| **`P`** | **The pellet he discarded**, washed once, resolubilised in 2 % SDS (or 8 M urea, ≤ 50 °C — `M5`), sonicated to shear DNA | 🔴 **`SOL-3`: nobody has ever looked in a WWOX pellet, for any allele, in any system** (`q230p_true_frontier_20260922.md:97`). This lane is the whole experiment |
| **`T`** | Paired well scraped **directly** into SDS/DTT, **no spin, no wash** | The only lane with **no discard step**. `S + P ≈ T` in the control lane is the design's own validity gate — falsifier **`F1`** (`minimum discriminator` §3.4): **if `S + P ≪ T` in the CONTROL lane, no double blank may be read at all and the run is void** |

### 3.2 Lanes on the gel

| # | Lane | Note |
|---|---|---|
| 1–3 | **Control fibroblast** — `S`, `P`, `T` | 🔴 **Two unrelated control donors is the correct minimum** (*"one control line is a donor, not a control"*). Compressing to one donor is permitted **only** with that loss written down |
| 4–6 | **`Q230P` fibroblast** — `S`, `P`, `T` | `HUMAN_REQUIRED` material (`M7`) |
| 7 | **WWOX-null / WWOX-silenced** (`T` only) | Band identity in dirty resolubilised pellets. `M6`: if it is a knockdown, this lane is *reduced*, not *null* |
| 8–13 | **Dilution series, ≥ 5 points + blank**, of a control-fibroblast lysate, **on the same membrane** | Gives the floor. `M4`: in **cell-equivalents** unless a quantified standard is sourced |
| — | **Loading** | 🔴 **Equal cell-equivalents, never equal protein** (`S`, `P` and `T` have different protein content **by construction** — that is the variable). Total-protein stain, **never β-actin**: actin partitions differently between `S` and `P` |
| — | **Replicates** | 3 biological, independent passages |

### 3.3 🔴 The smallest antibody configuration THAT ACTUALLY EXISTS

> **Primary channel — `HPA050992` (rabbit, aa 32–110, N-terminal).** The only orderable anti-WWOX
> antibody with an epitope placed relative to residue 230, and — census §4.1 row 3 — **the antibody
> that once converted a published WWOX "no protein" into a detected band.**
>
> **Second channel — `sc-20528` (goat, epitope constrained only at the extreme C-terminus).** Not
> chosen because it is good. Chosen because it is **Johannsen's instrument**: it is the only reagent
> on earth that makes a new negative *the same measurement* as the founding negative, and it carries
> the census's only **CRISPR-KO-validated human specificity control**.
>
> **Two hosts ⇒ one membrane, two IR channels, no stripping** (§1.3).

🔴 **What is lost, stated because it must be:**
- **This is NOT a flanking pair.** One epitope is N-terminal; the other is **unplaced** relative to
  230. ⇒ **An N-terminal fragment and a full-length protein cannot be distinguished by epitope.**
  They are distinguished **only by band size**, which is why *"score by size, not signal"* stops
  being style advice and becomes the design's load-bearing rule.
- **A fold-dependent epitope loss in the SDR cannot be excluded by this pair** (`H6`). Only **M3**
  (fragment competition) reduces it, and M3 is a separate afternoon.
- **If `sc-20528` proves discontinued (M2), the design runs on ONE antibody.** It still answers the
  §3 question — *is there signal anywhere in the recoverable pool* — because that question is about
  **presence in a fraction**, not about which fragment. 🔴 **What a single-antibody run cannot do is
  adjudicate a disagreement between two reagents, i.e. branch (d) below becomes unreachable.**
- 🔴 **If both antibodies fail to see WWOX in the CONTROL `T` lane above the LOD, every row is void**
  (falsifier `F2`). Pilot the reagents before spending the `Q230P` material.

---

# TASK 4 · PREREGISTERED OUTCOME BRANCHES

🔴 **Written now, before any further literature search, before any material is obtained and before
any blot exists.** Persisted here so that a later result cannot be read back onto a prediction that
was never made. 🔴 **No branch below converts into recovered FUNCTION. `abundance ≠ function`, and
`solubility ≠ stability ≠ activity`. Not one of these outcomes licenses a single sentence about
whether a WWOX molecule does anything.**

| Branch | Observation | 🟢 What it SUPPORTS | 🔴 What it does NOT support |
|---|---|---|---|
| **(a)** | **`P` and/or `T` positive at ~46 kDa in `Q230P`, `S` negative**, control arithmetic `S + P ≈ T` intact, null lane clean | **The protein is made and is recoverable.** *"Absence of WWOX protein"* is re-scoped to **"absent from the RIPA-soluble fraction"** — exactly the wording `CLAIM 030` already carries under `PREMISE: DETECTION_FLOOR`. `H1` (nothing is made) is **refuted for this cell type**. `SOL-3` is answered **for the first time for any WWOX allele** | 🔴 **NOT** that the protein folds, binds `NAD⁺`, dimerises, localises correctly or has any activity. 🔴 **NOT** that a proteostasis boost is safe — the repository's own matrix says a boost on the **insolubility** branch is *"actively dangerous"*, so this branch, if anything, **raises** the safety bar rather than lowering it. 🔴 **NOT** that the species is an aggregate: an SDS-soluble pellet species is not a demonstrated inclusion, and no aggregation assay was run. 🔴 **NOT** transferable to neurons (`SOL-6`: an SDS-insoluble species has been shown to form **only in patient neurons and not in the same patients' fibroblasts**) |
| **(b)** | **`T` positive but the `S`/`P` split is anomalous** — e.g. `T` ≫ `S + P` in the **control** lane, or WT WWOX itself partitions heavily into `P` | **That the fractionation is not quantitative in these hands (`F1`), or that the partition axis is saturated at baseline (`F5`).** This is a **finding about the instrument**, and `T` exists precisely to produce it | 🔴 **NOT** a result about `Q230P` at all. 🔴 **No double blank may be read**, `H1` becomes unassignable, and the run must be repeated before any allele statement is made. 🔴 It must **not** be reported as *"WWOX is partly insoluble"* — the control lane is the one that failed |
| **(c)** | **All three fractions negative in `Q230P`, with a validated low floor**, both antibodies, control lanes strong, arithmetic intact | **That no WWOX species is recoverable from this cell type above the stated floor** — written **only** as *"below X (cell-equivalents \| ng), N = 3"*. `H5` (insoluble sequestration) becomes **strongly disfavoured in fibroblasts**. On `q230p_minimum_discriminator` §4.2 this is the row where *"the function question is not deferred — it is **EMPTY**"* | 🔴 **NOT** *"no protein is made"*: synthesis was not measured (`P4`, `PROD-1`), so `H2` (impaired translation) and `H3`/`H4` (immediate disposal) are **untouched and indistinguishable**. 🔴 **NOT** *"absent"* as an unqualified word — that is the sentence this entire programme exists to stop. 🔴 **NOT** a neuronal result. 🔴 **NOT** an exclusion of a species below the floor: a floor is a floor |
| **(d)** | **The two antibodies disagree** — one sees a band the other does not, or they see **different sizes** | **That at least one reagent is misreporting**, which is itself a publishable reagent finding and is **the single most likely way the founding negative gets explained**. The null/knockdown lane adjudicates identity; **M3 fragment competition** adjudicates epitope | 🔴 **NOT** that `Q230P` protein exists — not until the null lane says the band is WWOX. 🔴 **NOT** that `sc-20528` is the insensitive one: that is `IPOTESI` (§1.1 point 4) and this experiment can support it **only if `HPA050992` is the one that sees more**. If the disagreement runs the other way, the *lde*-based expectation is **refuted**, and that must be written down as a refutation |
| **(e)** | **The WT/control lane fails** — no WWOX above the floor in control `T` | 🔴 **Falsifier `F2`: the instrument cannot see the target. Every row is void.** Re-pilot antibody, load, transfer and exposure before anything else | 🔴 **Absolutely nothing about `Q230P`.** 🔴 A failed control lane must never be reported beside a mutant lane as though the mutant lane meant something |
| **(f)** *(added — it is the branch the five did not cover)* | **A band at an unexpected MOLECULAR WEIGHT** in `P` or `T` | That a species exists whose mass differs from 46 kDa — an N-terminal fragment, a modified form, or a non-specific band | 🔴 **NOT** WWOX until the null/knockdown lane removes it **and** the second epitope agrees. 🔴 With an N-terminal antibody and an unplaced second one, **a C-terminally truncated species cannot be distinguished from a cross-reacting protein by epitope logic alone.** This is the exact cell the non-existent flanking pair was supposed to own |

---

# TASK 5 · THE EXON-7 RNA MICRO-EXPERIMENT

**The question:** *is exon 7 present in the mature `WWOX` transcript?* Johannsen's two amplicons
**bracket exon 7 and cover neither** (`johannsen2018…:173`): *"The core assay stops at the end of
exon 6 (`c.605`); the 3′ assay starts at the beginning of exon 8 (`≥ c.755`)."*

🔴 **Both prior beliefs are refused up front.** Nothing here infers that exon 7 **is** skipped, and
nothing here infers that its junction is **normal**. Both are `UNKNOWN`, and the point of the assay
is that the existing data **cannot see either**.

## 5.1 Can Johannsen's own published primers be repurposed? 🟢 **YES — by cross-pairing them**

`DATO`, Johannsen Methods, verbatim (`johannsen2018…:155`–`:160`): two pairs, *"spanning either
**exon 4–6** (forward 5′-CCAACCACCCGGCAAAGATA-3′, reverse 5′-AATGCTGCACGCTACGGAG-3′) or **exon 8–9**
(forward 5′-ATGTACTCCAACATTCATCGCAG-3′, reverse 5′-GTCTCTTCGCTCTGAGCTTCT-3′)"*, amplicons **277 bp**
and **200 bp** on gel.

`INFERENZA` — **neither pair alone can see exon 7, but the FORWARD of pair 1 with the REVERSE of
pair 2 spans it entirely.** Position arithmetic, using only the repository's own exon map
([`missense_splice_reclassification_risk_20260921.md:81`](missense_splice_reclassification_risk_20260921.md)):

```
exon 4  c.231–409   exon 5  c.410–516   exon 6  c.517–605
exon 7  c.606–B     exon 8  c.B+1–1056  exon 9  c.1057–1245      754 ≤ B ≤ 843
```

- Pair 1 spans exons 4–6 ⇒ its **reverse** lies in exon 6 (`c.517–605`) ⇒ its **forward 5′ end** lies
  between `c.241` and `c.329` ⇒ **in exon 4**. `INFERENZA`, forced by the stated 277 bp.
- Pair 2 spans exons 8–9 ⇒ its **reverse** lies in exon 9 (`≥ c.1076`, allowing 20 nt of annealing).
- ⇒ **cross-amplicon ≈ 750–1005 bp**, containing **all of exon 7 including `c.689`**.
- ⇒ **exon-7 skipping shortens it by the full exon-7 length, 149–238 nt** — a shift trivially
  resolved on a 1.5 % agarose gel, and the identical readout class that Weisz-Hubshman 2019 used to
  demonstrate exon-6 skipping (593 → 504 bp).
- 🟢 **Zero new oligonucleotides if Johannsen's laboratory still holds the two pairs.** The sequences
  are published, so anyone else synthesises two standard 20-mers for a few euro.
- 🔴 **Declared caveats, none fatal:** (i) the two primers were designed for **different** PrimerBank
  pairs and their annealing temperatures were **not** reported together — one gradient PCR settles it;
  (ii) ~800–1000 bp is an **endpoint RT-PCR**, not a qPCR amplicon — that is fine, because the
  readout is **size on a gel**, not ΔΔCt; (iii) a long amplicon can under-represent the longer
  species when a shorter one competes, so a **size ratio must never be read as an isoform ratio**.

## 5.2 Weisz-Hubshman 2019's pair — 🎯 **it demonstrably reaches past exon 6, and the proof is the mutant band**

`DATO`, Methods §2.4 (`ft117_weiszhubshman2019_fulltext_read_20260923.md:248`–`:252`):
*"cDNA segment containing exon six was amplified with the primers 5′TGGTTGTGGTCACTGGAGCTA3′ and
5′AGGATGCACTGCGTTCGAC3′."* `DATO`, Results: **WT 593 bp · mutant 504 bp · difference 89 bp = exon 6**
(`:221`–`:223`).

`INFERENZA`, and it needs no sequence at all:

> **The reverse primer must anneal entirely 3′ of exon 6.** The *same pair* amplifies both the
> 593 bp WT product **and** the 504 bp exon-6-skipped product. A primer lying inside exon 6, or
> spanning the exon 6/7 junction, cannot anneal to a transcript that lacks exon 6. **Therefore the
> reverse primer lies wholly within exon 7 or beyond**, and by the same argument the forward primer
> lies wholly 5′ of exon 6. 🎯 **Exon-7 sequence is already inside a published, gel-validated,
> blood-RNA-compatible amplicon.**

🔴 **What is NOT determined, and what would determine it.** Whether the reverse primer sits **in
exon 7** or **in exon 8** is `UNKNOWN`. The arithmetic cannot close it: with `U + D = 504`
(`U` = transcript 5′ of exon 6 inside the amplicon, `D` = transcript 3′ of it) and `U` bounded only
by the unknown 5′UTR length of `NM_016373`, `D` lies anywhere in **19–485 nt**, while exon 7 is
**149–238 nt** long. 🔴 **This would be settled in sixty seconds by one BLAT/BLAST of the 19-mer
against `NM_016373` — and `NM_016373` is not reachable from this deployment (§0). No sequence was
reconstructed and no coordinate was invented.**

**Why it matters, and it matters a lot:**

| If the reverse primer is in… | then on `Q230P` RNA, exon-7 skipping would produce… | Quality of the readout |
|---|---|---|
| **exon 8 or 9** | a product **shorter by 149–238 bp** — a clean size shift beside the WT band | 🟢 **Excellent.** Same readout class as the paper's own 593/504 |
| **exon 7** | 🔴 **no product at all** — the primer site would be deleted | 🟡 **Ambiguous.** A dropout is indistinguishable from PCR failure without an independent amplification control in the same tube |

⇒ `INFERENZA`: **the cross-paired Johannsen primers (§5.1) are the safer design**, because the
reverse primer is in **exon 9** by construction and the readout is a **shift**, never a dropout.

🔵 **A small corroboration worth one line.** Weisz-Hubshman's qPCR pair is *"5′CTTTCACCAAGTCCATGCAA3′
and 5′CGTCTCTTCGCTCTGAGCTT3′"*, amplifying ex8–9 (`ft117…:355`–`:357`). Its reverse is the same site
as Johannsen's ex8–9 reverse (`GTCTCTTCGCTCTGAGCTTCT`), offset by one nucleotide. **Two independent
laboratories converged on the same 3′ anchor** — which also means the ex8–9 read is the field's
default and the exon-7 blind spot is **structural, not accidental**.

## 5.3 Material — the part that is genuinely unknown

| Asset | Status |
|---|---|
| Johannsen's **`Q230P` cDNA / RNA** | 🔴 **`UNKNOWN`.** The paper stores **protein** at −80 °C (*"the remaining material stored at −80 °C"*, `:61`); the RNA fraction's fate after 2018 is not stated anywhere. **`HUMAN_REQUIRED`: one email** |
| Johannsen's **fibroblast line** | 🔴 **`UNKNOWN`.** *"within five passages"*, two independent harvests — consistent with a cryopreserved stock, **stated nowhere**. `HUMAN_REQUIRED` |
| Johannsen's **primers** | 🟢 **Published verbatim. Re-synthesisable by anyone, today** |
| Weisz-Hubshman's **pair** | 🟢 **Published verbatim**, and validated on **blood-derived** RNA — i.e. it does not require a fibroblast culture at all |
| **`Q230P` RNA in this repository** | 🔴 **None. Zero.** Confirmed by yesterday's read (`johannsen2018…:316`) |

## 5.4 🟡 CLASSIFICATION: **`MINOR NEW ASSAY`**

**Not `EXISTING MATERIAL`** — no `Q230P` RNA exists in reach, and whether the original cDNA survives
is `UNKNOWN`. **Not `NEW MATERIAL`** in the design sense — **no assay has to be designed**: two
published primer pairs already bracket exon 7 and one cross-pairing of them covers it, and a second
published pair already reaches into it. **Not `UNKNOWN`** — the arithmetic above is determinate on
the one point that matters (exon 7 is reachable with published oligos).

> **One RT-PCR tube, published primers, a 1.5 % gel. If a `Q230P` RNA aliquot exists anywhere, this
> is a single afternoon and a few euro of oligos.** It is by a wide margin the cheapest open
> question in the `Q230P` file, and it is cheaper than every protein experiment above.

🔴 **Two things it would and would not tell you, and they must not be merged.**
1. A product of **WT size** ⇒ exon 7 is **present in the mature transcript**. 🔴 It does **NOT**
   establish that the junction is normal at nucleotide level — a cryptic site shifting the boundary
   by a few nucleotides, or any in-frame micro-alteration, would be size-indistinguishable.
   **Only Sanger sequencing of the product establishes the junction**, and the cross-paired amplicon
   covers `c.689` so the same read also re-confirms the variant in cDNA.
2. A **shortened** product ⇒ a skipped species **exists**. 🔴 It does **NOT** give its fraction, and
   band intensity in a long competitive amplicon is **not** a ratio (§5.1 caveat iii). And it would
   **not**, by itself, explain the protein result: `RNA-4` remains a hypothesis about splicing, not
   a mechanism for absent protein.

---

## 6 · `UNKNOWN`s, declared as `UNKNOWN`

1. 🔴 **Is `sc-20528` a current Santa Cruz catalogue item in 2026?** `UNKNOWN — VENDOR DATASHEET BLOCKED`.
2. 🔴 **Is `HPA050992` still listed by Sigma-Aldrich?** `UNKNOWN — VENDOR DATASHEET BLOCKED` (`RT-AB-04`, open since 2026-09-22).
3. 🔴 **Where is `sc-20528`'s epitope relative to residue 230?** `UNKNOWN`. All that is known is a 2009 vendor personal communication excluding the region altered by `p.Leu371Thrfs*53`.
4. 🔴 **The catalogue numbers of the ProteinTech (`A5`) and Abcam (`A6`) antibodies.** `UNKNOWN` — `HUMAN_REQUIRED`, author correspondence.
5. 🔴 **The epitopes of `ab238144`, `ab189410`, `ABN413`, `4045S`, `ab216660`.** `UNKNOWN` — every route is a datasheet, all 403 today.
6. 🔴 **Does a quantified recombinant human WWOX protein standard exist commercially?** `UNKNOWN`.
7. 🔴 **Does `HPA050992` work on a human fibroblast lysate?** `UNKNOWN` — every WB attested in sources read here is rat tissue.
8. 🔴 **Is the Weisz-Hubshman reverse primer in exon 7 or exon 8?** `UNKNOWN` — needs `NM_016373`, unreachable (§0).
9. 🔴 **Does Johannsen's `Q230P` RNA/cDNA or fibroblast stock still exist?** `UNKNOWN` — one email.
10. 🔴 **Is exon 7 present in the mature `Q230P` transcript?** `UNKNOWN`, in **both** directions. Nobody has looked.

### 6.1 `REVIVAL_TRIGGER`

| # | Statement | What would overturn it |
|---|---|---|
| `RT-EX-01` | *"`A5`/`A6` are not orderable"* | Either catalogue number, from the authors or from a reachable vendor search |
| `RT-EX-02` | *"The smallest existing configuration is `HPA050992` + `sc-20528`"* | Any reachable datasheet placing one of the five orderable-but-unstated antibodies **C-terminal to 230** — that single fact restores the flanking pair and upgrades Task 2 |
| `RT-EX-03` | *"`sc-20528` may be the less sensitive reagent"* — `IPOTESI` only | The two antibodies run side by side on one membrane (§3.3). **Either outcome is informative; the refutation must be recorded as such** |
| `RT-EX-04` | *"Cross-paired Johannsen primers give ~750–1005 bp"* | Any measured product size; the bracket rests on the unfixed exon 7/8 boundary `B` and on 20 nt annealing assumptions |
| `RT-EX-05` | *"`A17` ≡ `A21`"* | A statement from either laboratory that a different lot/reagent was used, or a second Santa Cruz anti-WWOX with the same number |

### 6.2 `HUMAN_REQUIRED` — nothing was contacted, nothing was bought

**(i)** Open the `HPA050992` and `sc-20528` catalogue pages; confirm listing, applications and — for
`sc-20528` — **the immunogen field, which would close `UNKNOWN` #3 and possibly `RT-EX-02`.**
**(ii)** Email Davids 2019 for the two catalogue numbers (`A5`, `A6`).
**(iii)** Email Johannsen 2018: does `Q230P` RNA/cDNA or a cryopreserved fibroblast stock survive?
**(iv)** One BLAT of `AGGATGCACTGCGTTCGAC` against `NM_016373` — sixty seconds, closes `UNKNOWN` #8.

---

## 7 · DECLARED LIMITS OF THIS FILE

- **Bounded audit.** Two retrieval calls were made in total (one PubMed, one Scholar Gateway), both
  aimed at a single catalogue number. **No discovery wave, no refill, no corpus sweep.**
- The Suzuki 2009 passage was read as a **publisher-served passage body**, not as a local full text,
  and its text layer deletes hyphens and superscripts. **Characters were not altered**; the catalogue
  number is rendered `sc20528` in the source and is written `sc-20528` here, consistent with the
  census's already-recorded typesetting note on Johannsen's `sc20,528`.
- 🔴 **No first-hand vendor information of any kind entered this file.** Every listing status is
  `UNKNOWN`.
- 🔴 **No sequence was reconstructed.** Every primer position is either arithmetic on published
  amplicon sizes and the repository's own exon map, or `UNKNOWN`.
- **On Weisz-Hubshman 2019, the bounded formulation is used** and the earlier phrasing is not
  repeated: sequencing is stated in the abstract **and** in Methods §2.4; the Results section
  documents the splice consequence primarily through the 593/504 bp products and the stated 89 bp
  exon-6 deletion, without displaying a junction chromatogram or narrating its sequence.
  `c.517-2A>G → exon-6 skipping` stands as supported by the paper as a whole.
- **No canonical file, registry, queue, `*_current.md`, receipt ledger, state manifest,
  Operator-gated commit candidate or discovery-method V0 file was modified.** The deltas owed to
  `wwox_antibody_epitope_census_20260922.md` (§1.1) are **stated here and applied nowhere**.
- 🔴 **Nothing in this file is medical advice, and no outcome branch in §4 licenses any statement
  about WWOX function, therapeutic benefit or clinical course.**
