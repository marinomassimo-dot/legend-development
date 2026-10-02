# COMMIT CANDIDATE — CC-20261002-WWOX-DOSE-CEILING-01

**Candidate ID:** CC-20261002-WWOX-DOSE-CEILING-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-c`, 2026-10-02, intake wave 2026-10-02.
**Change class:** **MINOR.** It narrows no claim and reverses none. It records an **absence** next to
a claim that is already `flagged for review`, and adds one bullet to `BLOCK 1 §4`. No claim changes
status, no working-model block is redefined, no therapeutic score moves.
`context_policy: SOURCE_FIRST` — every source below was read and written up before the model's
safety layer was opened.

**Not medical advice.**

---

## 0 · The question this answers

*"Does any source say what happens when WWOX is increased, and how far does that transfer to a
neuron-targeted gene-therapy setting?"*

**The short answer: three sources say that raising WWOX can do harm or fail to help, none of them
in a neuron-targeted vector setting, and the model currently records none of them — nor records
that it records none of them.**

## 1 · The readings this rests on

| Record | What it actually shows about *raising* WWOX | Evidence class |
|---|---|---|
| **PMID 42395553** (Petrozziello 2026, **bioRxiv preprint, not peer reviewed**) | Applied recombinant WWOX protein killed human ESC-derived cortical neurons at 100 ng/mL, **in HD and isogenic control neurons alike** (no treatment×genotype interaction). Applied protein ≥100 ng/mL and a stable transgene both raised γ-H2AX in SH-SY5Y | **Extracellular applied protein** in neurons; **transgene** only in a neuroblastoma line and RPE-1. No in vivo arm, no vector, no dose |
| **PMID 37781246** (Kałuzińska-Kołat 2023) | Lentiviral WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines (DBTRG-05MG) — opposite to the other three | Cancer cell lines; and the phenotype is **cited from the group's preceding paper**, not measured here |
| **PMID 33195192** (Chou 2020) | States context-dependence explicitly, and cites Nowakowska 2014 (HT29): raised WWOX increasing proliferation | Review statement + **citation to an unread source** |

Receipts `FTR-20261002-42395553-01`, `FTR-20261002-37781246-01`, `FTR-20261002-33195192-01`;
manifests `PMID42395553.json`, `PMID37781246.json`, `PMID33195192.json`, all schema v2, strict
PASS, 0 gaps, artifacts verified on disk.

## 2 · What the model currently says, and what it does not

`CLAIM 011` and `BLOCK 1 §4` reason about dose **in one direction only**, and they do it very
carefully: *"below 2.63 × 10¹¹ vg survival is not rescued at all"*, and *"An inference of the form
'a lower, safer dose would still help' reads the dose-response as continuous and Figure 3B refuses
it for survival in this model."*

That sentence rebuts one reason for wanting a lower dose — that it might be safer — by showing the
survival curve refuses it. **It does not address whether an upper bound exists.** No canonical
record, in any direction, states a consequence of raising WWOX. The corpus cross-query returned
**0 hits** for that question.

🔴 **The honest finding is a negative one about this batch, and it is stated first:** none of the
three sources above **bounds** `CLAIM 011` or `BLOCK 1 §4` as written, and this candidate does not
claim that they do.

- The preprint has no vector, no in vivo arm and is not peer reviewed; its *neuronal* datum uses
  extracellular recombinant protein, which is not what a vector delivers, and it reports **no**
  heat-denatured, tag-only or endotoxin control — the controls that would separate "WWOX" from "a
  commercial protein preparation".
- The glioblastoma result is in heavily mutated cancer lines, and its authors explicitly refuse the
  causal reading.
- Against all of it stands Obeid 2026 *in vivo*: neuron-targeted AAV9-hSynI-hWWOX at the high dose
  gave ~80% survival to 300 days with no reported overexpression toxicity. That is a stronger
  evidence class than a 24-hour MTT on cultured neurons, and it stands.

**What changes is not the claim. What changes is that the model stops being silent about a
question it has never asked.**

## 3 · Ops

### Op 1 — `claim_registry_current.md`, record `CLAIM 011`, APPEND to the `Impact on Working Model` line

`old` (verbatim, measured unique **in its record** and in the file):
```text
**Impact on Working Model:** BLOCCO 2 integrated; gene therapy context section updated in BLOCCO 1
```

`new`:
```text
**Impact on Working Model:** BLOCCO 2 integrated; gene therapy context section updated in BLOCCO 1
⚠️ **`PREMISE_TAG` added 2026-10-02 (`CC-20261002-WWOX-DOSE-CEILING-01`, intake wave 2026-10-02) — the dose reasoning in this claim has a floor and no ceiling, and that is an absence of evidence, not evidence of absence.** Every dose statement here, and every one in `BLOCCO 1 §4`, concerns clearing a threshold; **no source in this corpus measures what happens above the high dose**, and Obeid 2026 reports no overexpression-toxicity endpoint at all. 🔴 Three sources outside the vector setting now record that raising WWOX is not uniformly benign: applied recombinant WWOX protein reduced viability of human ESC-derived cortical neurons at 100 ng/mL **equally in disease and isogenic control cells** (PMID 42395553 — ⚠️ **bioRxiv preprint, NOT peer reviewed**; extracellular applied protein, **not** a transgene, **no** heat-denatured or endotoxin control reported, no in vivo arm); lentiviral WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines (PMID 37781246, and that phenotype is cited from the group's preceding paper, not measured there); and the same two-sided proposition is stated independently in 2020 — *«A certain amount of WWOX expression may be necessary for maintaining normal physiological functions in cells.»* (PMID 33195192) — which also cites, without measuring, raised WWOX increasing proliferation in HT29 (Nowakowska 2014, unread). 🟢 **None of this bounds the claim as written and none of it is carried as a hazard:** no source has a vector, a delivered dose, a neuron-targeted transgene or an in vivo endpoint, and the one in vivo result in the corpus is ~80% survival to 300 days at the high dose. ⚠️ Note separately that `PAPER 082` (Fabbri 2005), one of the citations behind the general belief that restoring WWOX is benign, stands under `PUBLICATION_INTEGRITY_HOLD` — narrow scope, one panel, not a retraction — which is a reason not to treat that belief as more heavily evidenced than it is. `REVIVAL_TRIGGER`: **any** arm that raises neuronal WWOX above the Obeid high dose and reports a toxicity endpoint; or a repeat of the rWWOX neuron experiment with a heat-denatured-protein control; or a peer-reviewed version of PMID 42395553.
```

### Op 2 — `working_model_current.md`, `BLOCK 1 §4`, APPEND one bullet

`old` (verbatim, measured unique in the file):
```text
- **Partial rescue is expected to be beneficial** in genotype classes retaining a missense allele (Gao 2025 genotype–phenotype suggests partial restoration may suffice).
```

`new`:
```text
- **Partial rescue is expected to be beneficial** in genotype classes retaining a missense allele (Gao 2025 genotype–phenotype suggests partial restoration may suffice).
- ⚠️ **The dose reasoning above has a floor and no ceiling, and nothing in this corpus has measured one** [added 2026-10-02, `CC-20261002-WWOX-DOSE-CEILING-01`]. Obeid 2026 reports no overexpression-toxicity endpoint, and no claim in this model states any consequence of *raising* WWOX. Outside the vector setting, three sources now say raising it is not uniformly benign — applied recombinant WWOX protein reduced viability of human ESC-derived cortical neurons **equally in disease and isogenic control cells** (PMID 42395553, ⚠️ **preprint, not peer reviewed**, applied protein rather than a transgene, no heat-denatured or endotoxin control reported, no in vivo arm); WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines (PMID 37781246); and *«A certain amount of WWOX expression may be necessary for maintaining normal physiological functions in cells»* (PMID 33195192). 🟢 **None of this changes a dose position, and none of it is a hazard claim** — no source has a vector, a dose or an in vivo endpoint. It is recorded so that the absence of a ceiling is visible as an open question rather than as a settled one. See [[claim_registry_current#CLAIM 011]]. **Not medical advice.**
```

## 4 · What would falsify this candidate

If a reader finds any existing canonical record that already states a consequence of raising WWOX,
Op 1 and Op 2 are redundant and should be dropped. The cross-query that returned 0 is recorded in
`PMID42395553.json` → `corpus_crossquery` and can be re-run.

## 5 · Deliberate non-ops

- **No new claim is created.** A measured absence beside an existing claim is the proportionate
  vehicle; a `CLAIM 043` for "nobody has looked" would give the absence the shape of a finding.
- **No dismissal-ledger entry.** This is not a rejection; `DIS-003` already rejects *boosting WWOX
  expression* on a different and still-valid ground (Johannsen 2018: normal transcript, protein
  absent — the bottleneck is downstream), and nothing here touches that reasoning.
- **No therapeutic-tracker change.** Gene therapy's position is unchanged.

---

### LOCATOR TRIPLES FOR BLIND AUDIT

(Artifacts confirmed present on disk, SHA-256 verified, every snippet matched character-exact by
`deepdive_manifest.py --verify-artifacts`. ⚠️ The `PMID42395553…txt` surface spells the Greek gamma
as a Latin `g` and preserves line-break hyphenation as hyphen-plus-space.)

1. (Applied recombinant WWOX protein was cytotoxic to the cell line in a dose- and time-dependent way | `Treatment with rWWOX caused cell death in a dose- and time-dependent manner in SH- SY5Y cells, with significant decreases observed at 100 or 500ng/mL after 24h and at 10, 100 or 500ng/mL after 48h` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Results, "Increases in WWOX induce neuronal toxicity in HD ESC-derived cortical neurons", first result paragraph)

2. (The viability loss in human cortical neurons occurred in the disease line and in its isogenic control alike | `Our results revealed a significant decrease in cell viability in both rWWOX-treated HD cortical neurons (65Q) and their isogenic controls (27Q) compared to the respective vehicle- treated cells` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Results, same paragraph)

3. (There was no interaction between treatment and genotype | `Two-way ANOVA revealed a significant effect of treatment [F(1, 28)=78.44; p<0.0001], and genotype [F(1,28)=6.181; p=0.0192], with no significant treatment x genotype interaction [F(1,28)=0.3129; p=0.5804]` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Figure 4 legend, panel B)

4. (The material applied to the cells was a purchased recombinant protein, given at these concentrations | `Recombinant full-length human WWOX protein (rWWOX) was purchased from Pepmic Co (Suzhou, China). Cells were incubated with 1, 10, 100 or 500ng/mL rWWOX for 24h or 48h before measuring cell viability by MTT assay` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Material and Methods, "SH-SY5Y cell culture treatments", Recombinant protein treatment)

5. (The DNA-damage marker responded above a concentration threshold and not below it | `While treatment with 10ng/mL of rWWOX did not alter g-H2AX levels (Tukey's test, p=0.6018), treatment with either 100ng/mL (Tukey's test, p=0.0139) or 150ng/mL of rWWOX (Tukey's test, p=0.0038) significantly increased g-H2AX levels compared to vehicle-treated cells.` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Figure 5 legend, panel B)

6. (The authors conclude that elevated levels can promote damage and that the level matters | `our findings indicate that elevated WWOX can also promote DNA damage. Together, these observations suggest that maintaining appropriate WWOX levels may be important for cellular homeostasis.` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Discussion, paragraph on complementary approaches)

7. (The authors decline to state a direction for modulating the protein | `Defining the relationship between mutant HTT and WWOX will be important to determine whether modulation of WWOX can mitigate disease-relevant phenotypes.` | `files/fulltext/PMID42395553_Petrozziello2026_bioRxiv.txt` · Discussion, limitations paragraph)

8. (Overexpression raised proliferation in only one of the four cell lines | `proliferative potential after WWOX overexpression was increased only in DBTRG-05MG` | `files/fulltext/PMID37781246_KaluzinskaKolat2023_PMC.xml` · Results and discussion, WWOX-related network section)

9. (The authors refuse the inference that the higher level caused the worse outcome | `the elaborated resemblance of findings from GBM cell lines using data from GBM patients is imperfect, and it cannot be assumed that POLE4 and HSF2BP levels were elevated in patients with unfavorable outcomes due to the higher levels of WWOX` | `files/fulltext/PMID37781246_KaluzinskaKolat2023_PMC.xml` · Results and discussion, final paragraph of the patient-stratification section)

10. (A high level together with other elevated genes brought no prognostic benefit in one patient group | `high WWOX expression with simultaneously elevated expression of other genes (herein: POLE4 and HSF2BP ) did not bring prognostic benefits and may be related to the more cancer-promoting profile` | `files/fulltext/PMID37781246_KaluzinskaKolat2023_PMC.xml` · Conclusion, final paragraph)

11. (The effect of the protein on growth and apoptosis is stated to depend on the cell context | `the control of cell growth and apoptosis by WWOX may depend on cell types, such as their tissue origin, differentiation state or differences between normal, benign and malignant cells` | `files/fulltext/PMID33195192_Chou2020_PMC.xml` · Discussion, paragraph on pleiotropic functions)

12. (In one colon adenocarcinoma line a raised level is reported to increase proliferation and inhibit apoptosis | `in low-grade invasive HT29 colon adenocarcinoma cells, increased WWOX expression promotes cell proliferation but inhibits apoptosis` | `files/fulltext/PMID33195192_Chou2020_PMC.xml` · Discussion, same paragraph, citing Nowakowska et al. 2014)

13. (A particular quantity, rather than simply more, is stated to be what normal function requires | `A certain amount of WWOX expression may be necessary for maintaining normal physiological functions in cells.` | `files/fulltext/PMID33195192_Chou2020_PMC.xml` · Discussion, sentence following the cell-type dependence sentence)
