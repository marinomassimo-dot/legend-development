# CC-20261004W11-A-SDRCLUSTER-01 — a 17β-HSD family assignment does not deliver a substrate, and a WWOX oxidoreductase assay has a measured endogenous floor

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist A of intake wave 11,
2026-10-04. **Source:** PMID 40336300, receipt `FTR-20261004-40336300-01`, manifest
`deepdive_manifests/PMID40336300.json` (7 locators, strict PASS, 0 gaps).
**Change class: MINOR** — it qualifies an open, non-canonical discovery-ledger lead and touches no
`consolidated baseline` claim. **Nothing here is medical advice.**

## 1 · The transfer, and its limit, before anything else

**WWOX occurs zero times in this source.** That is an earned null for the gene: the paper does not
mention, test or model WWOX, and WWOX is absent even from its proteomic census of testicular
hydroxysteroid dehydrogenases. Everything below is a statement about **17β-hydroxysteroid
dehydrogenase enzymology in general**, transferred only to the *method* by which the corpus should
judge a WWOX substrate or activity claim — never to a WWOX number, never to a WWOX residue, and never
across alleles (P47T ≠ Q230P ≠ G372R ≠ A141T ≠ P252A).

## 2 · Why it bears on the open question

Wave 10's reading of PMID 21476439 concluded that the WWOX SDR-substrate claim rests on one
laboratory's crude-extract assay and on motifs cited to a paywalled, unread 2000 paper, and that the
regiochemistry attributed to WWOX derives from clustering WWOX with 17β-HSD enzymes. This source is
the first orthogonal test in the corpus of **how much such clustering is worth**, and it gives three
measured answers:

1. **One residue decides substrate entry.** Human and primate HSD17B12 carry a phenylalanine at
   position 234 that blocks C19-steroid entry into the active site; the mouse leucine does not.
   Orthologous enzymes, same family, same fold, opposite substrate acceptance — and the paper proves
   it causally by substituting the residue and losing the activity. **A family assignment is therefore
   a hypothesis about substrate, not a determination of one.**
2. **A published substrate negative in this family was overturned by assay conditions.** Two earlier
   studies concluded that mouse HSD17B7 cannot convert androstenedione to testosterone; this paper
   reports the conversion and attributes the earlier negatives to lower substrate concentration and
   shorter incubation. **In this enzyme family, a single-condition result — positive or negative — is
   not a determination.**
3. **The assay floor is not zero.** Untransfected and eGFP-control HEK-293T cells produce testosterone
   from androstenedione, which the authors attribute to endogenous hydroxysteroid dehydrogenase
   activity. **An activity measured in a whole cell or a crude extract includes that floor unless a
   catalytically dead control subtracts it.** The same authors write the remedy as their own
   prerequisite: identify the residues responsible, then mutate them.

## 3 · Proposed op (append-only; the discovery ledger is append-only on leads)

- **file** `disease-models/wwox/research/discovery_ledger_current.md`
- **record** `DL-BIO-001`
- **op** append (a dated block at the end of the record, in the style the record already uses for its
  2026-09-21 and 2026-09-27 updates; nothing existing is replaced or deleted)
- **new** (content, not formatting):
  > ⚠️ **Qualification of the enzymatic arm — 2026-10-04 (intake wave 11, Scientist A, from PMID 40336300, receipt `FTR-20261004-40336300-01`; WWOX occurs zero times in that source and nothing about WWOX is imported from it).** This lead proposes an **oxidoreductase activity assay** on donor-derived fibroblasts as the secondary readout beside protein quantity. An orthogonal 17β-HSD paper now bounds what such an assay can mean, on three measured points about that enzyme family: (i) **substrate acceptance turns on single residues** — human and primate HSD17B12 carry a phenylalanine at position 234 that blocks C19-steroid entry while the mouse leucine does not, so WWOX's membership of the SDR/17β-HSD family predicts no substrate and the regiochemistry the corpus carries for WWOX remains **predicted, not measured**; (ii) **a substrate negative in this family is condition-dependent** — two published studies concluding that mouse HSD17B7 cannot use androstenedione were overturned by raising substrate concentration and lengthening incubation; (iii) **the assay floor is not zero** — untransfected control cells convert the substrate through endogenous hydroxysteroid dehydrogenases, so an activity measured in fibroblast lysate carries an endogenous background that only a **catalytically dead WWOX control** can subtract. **Consequence for the experiment already written above:** the oxidoreductase arm is not executable as written. Before it is run it needs (a) a named substrate and cofactor with a stated concentration and incubation, (b) a catalytically dead WWOX control (the YxxxK catalytic motif is the obvious target), and (c) a substrate titration rather than one condition. Until those exist, **protein quantity and stability remain the primary readout, and the enzymatic arm stays a hypothesis-grade readout, not a biomarker.** Per `LEGEND_CORE` §13, a direct enzymatic-activity readout of WWOX would be Tier 1 **if it measured WWOX**; an assay that cannot separate WWOX activity from an endogenous floor does not yet measure the functional state of the gene and must not be described as validated.

## 4 · What must NOT be written from this source

- Not "HSD17B7 or HSD17B12 work bears on WWOX": the paper does not mention WWOX, and no WWOX-specific
  inference is drawn from it here.
- No transfer of any mouse enzymology to a human enzyme — the paper's own closing position is that the
  human orthologues have lost this redundancy.
- No kinetic constant: the paper measures none.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

A single residue decides whether a C19 steroid can enter the active site of an otherwise orthologous 17β-HSD enzyme. | In human and primate HSD17B12, a bulky phenylalanine amino acid at this location prevents the entrance of C19-steroids into the active site of the enzyme | Introduction, sixth paragraph — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

A published negative on substrate use by a member of this enzyme family was overturned in this paper. | Two earlier studies concluded that mouse HSD17B7 did not perform this conversion | Discussion, paragraph on HSD17B7 — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

The authors attribute those earlier negatives to assay conditions rather than to the enzyme. | those studies employed reduced concentrations of substrate and shorter incubation times, which may have influenced the observed outcomes | Discussion, paragraph on HSD17B7 — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

Cells carrying no transfected enzyme still convert the substrate, so a cell or crude-extract activity assay has a non-zero endogenous floor. | Non-transfected cells and eGFP controls produced low levels of testosterone upon addition of androstenedione, suggesting some endogenous hydroxysteroid dehydrogenase activity in HEK-293T cells | Results, Replacement of Leucine With Phenylalanine at Position 234 Inhibits Testosterone Biosynthesis in Mouse HSD17B12 — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

Members of this family are multifunctional, so naming one substrate does not define the enzyme's chemistry. | HSD17B7 is a multifunctional enzyme that can utilize estrone, DHT and zymosterone as substrates | Discussion, paragraph on HSD17B7 — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

Attributing a conversion to one family member requires identifying the responsible residues and mutating them, by the authors' own statement. | would first require the identification of the specific amino acid residues responsible for the conversion of androstenedione to testosterone | Discussion, paragraph on HSD17B7, future work — files/fulltext/PMID40336300_Lawrence2025_PMC.xml

Mouse and human orthologues differ in this redundancy, so a mouse enzymology result does not transfer unexamined. | human orthologs have lost this plasticity | Discussion, final paragraph — files/fulltext/PMID40336300_Lawrence2025_PMC.xml
