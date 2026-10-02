# COMMIT CANDIDATE — CC-20261003-C-STEINBERG-PANELS-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 2 2026-10-03, branch `task/sci-C-20261003`.
**context_policy:** `SOURCE_FIRST`; prior knowledge admitted after the first pass by `registry_records.py get --pmid 34268881`.
**Not medical advice.**

## Target

- `research/discovery_ledger_current.md`: **create** one lead, provisionally `DL-METH-116`, recording six
  text-versus-panel disagreements in PMID 34268881 that the corpus did not hold.

No claim, no working-model block, no paper record is edited by this candidate. `DL-MECH-098` and
`DL-THER-105` already carry the 2026-08 findings on this paper and are **not** touched: nothing
below contradicts them.

## Change class

**MINOR** (§ 7). A research-layer lead about source-internal reporting defects. It narrows no
`consolidated baseline` claim. Two of the six items do, however, bear on sentences that other
records may have quoted, which is why they are written down rather than left in a dossier.

## Ordering

`FTR-20261003-34268881-06` must be in the ledger before this record lands.

## The six items

Each was found by inspecting the twelve distributed figure images and the Appendix, and each is a
disagreement between the paper's running text and its own quantification. None is a data defect;
five are reporting defects and one is an internal disagreement between two panels of one figure.

1. **4-AP is not inert in wild type.** Results: *"the KO line showed significantly increased
   activity, which was otherwise absent in WT traces (Fig EV1J)"*. Panel EV1J draws a significance
   marker on **both** genotypes — WT ≈0.022 → ≈0.067 (`*`), KO ≈0.072 → ≈0.100 (`*`) — so the
   convulsant raises wild-type power about threefold against about 1.4-fold in the knockout.
   **Consequence for LEGEND:** a 4-AP challenge does not separate the genotypes in this model; the
   **baseline** 0.25–1 Hz AUC does. Any protocol built on "4-AP unmasks the WWOX phenotype" is
   building on a sentence its own panel contradicts.
2. **The high-frequency decrease is not significant.** Results assert *"a decrease in the 30- to
   79.9-Hz high-frequency range (Fig EV1G and H)"* and the Discussion builds a paragraph on it.
   Panel EV1H is marked **n.s.** (WT ≈0.0098, KO ≈0.0035, 14 slices each).
3. **Cortical-layer nomenclature is inverted in the Results.** The text calls
   TBR1/BCL11B/SATB2/POU3F2 *"layers I-IV"* and CUX1/RELN *"superficial layers V-VI"*. The
   paper's own Fig 4F legend orders the same six markers *"from deepest to the most superficial"*,
   i.e. TBR1 deep, CUX1/RELN superficial — the standard assignment. **Anyone carrying "deep layers
   up, superficial down" out of this paper carries it backwards.**
4. **The SCAR12 null is softer than the text.** Results report no significant astrocytic
   difference (Fig EV5A/B) and comparable cortical markers (Fig EV4C). Fig EV5B marks **GFAP and
   ALDH1A1 significant** in one affected sibling; Fig EV4C marks **SATB2 significant in both**
   affected siblings and RELN in one; and Appendix Table S1, for the forebrain comparison it does
   cover, gives GFAP `P = 0.0311`, S100B `P = 0.0237`, AQP4 `P = 0.0077`, ALDH1A1 `P = 0.0061`.
   The claim that the platform cleanly separates SCAR12 from WOREE is a difference of degree.
5. **Appendix Table S1 does not cover the main figures.** Methods: *"Exact P-values and the
   specific tests used are stated in Appendix Table S1."* The distributed table lists exact
   P-values for Appendix Figs S2A, S3C, S4E and S5D/F/H/I **only**. **No main-figure or
   Expanded-View P-value is distributed anywhere**: every effect size cited from Figs 1–6 and
   EV1–EV5 is read off an asterisk-banded plot.
6. **The GABAergic rescue is protein-only.** Fig 1F restores GAD67 area per nucleus in the W-AAV
   line (≈1.0 → ≈0.1, `****`); Fig 1D leaves *GAD1* transcript at ≈7.5-fold of wild type in the
   same line (KO ≈8.5-fold). The text records both as having *"followed the same trend"*.

## One absence, stated as an observation

The gene symbol `WWOX` appears in **neither** Expanded-View differential-expression table
(`-s006.xlsx`, 1,246 up; `-s005.xlsx`, 1,021 down; both opened and checked for symbol
membership). An exon-1 frameshift with a premature termination codon would be expected to show
nonsense-mediated decay. The knockout is evidenced by immunoblot, not by the transcriptome
published beside it. This is an observation about the deposited tables, **not** an allegation
about the knockout.

## What this does not do

- It does not retract or downgrade any finding of the paper, and it does not touch
  `DL-MECH-098`, `DL-THER-105` or `PAPER 039`.
- It does not claim the gamma result is wrong — only that it is unquantified.
- It does not close `FT-059`. `FT-059` records that 69 figure panels were never read; the 2026-08
  addendum to `research/fulltext_dossiers/PMID34268881.md` already reports reading all of them,
  and this reading independently inspected all twelve distributed figure images. Reconciling the
  queue entry with that history is the Orchestrator's, not a Scientist's.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 against `f5f946837924`)

```json
[
 {
  "op": "append",
  "text": "\n### DL-METH-116 — Sei disaccordi testo-contro-pannello in Steinberg 2021, e cosa cambiano per chi lo cita\n\n- **Status**: open · **Tag**: DATO (ciascun pannello) + METODO · **Fonte**: intake wave 2 2026-10-03, Scientist C — PMID 34268881, dodici immagini di figura distribuite ispezionate, Appendix e tabelle Expanded View aperte. Nessuno di questi sei punti era nel corpus; nessuno contraddice DL-MECH-098 o DL-THER-105.\n- **1. Il 4-AP non e' inerte nel wild type.** Il testo dice che la linea KO mostra attivita' aumentata 'which was otherwise absent in WT traces (Fig EV1J)'. Il pannello EV1J disegna un marcatore di significativita' su ENTRAMBI i genotipi: WT da circa 0,022 a circa 0,067 (*), KO da circa 0,072 a circa 0,100 (*). Il convulsivante alza la potenza del wild type circa tre volte contro circa 1,4 volte nel KO. CONSEGUENZA: una sfida con 4-AP non separa i genotipi in questo modello; lo fa la potenza BASALE a 0,25-1 Hz.\n- **2. La riduzione in alta frequenza non e' significativa.** Risultati e Discussione asseriscono 'a decrease in the 30- to 79.9-Hz high-frequency range' e vi costruiscono sopra un paragrafo; il pannello EV1H e' marcato n.s. (WT circa 0,0098, KO circa 0,0035, 14 fette per braccio).\n- **3. La nomenclatura degli strati corticali e' invertita nei Risultati.** Il testo chiama TBR1/BCL11B/SATB2/POU3F2 'layers I-IV' e CUX1/RELN 'superficial layers V-VI'. La didascalia della Fig 4F dello stesso paper ordina gli stessi sei marcatori 'from deepest to the most superficial', cioe' TBR1 profondo e CUX1/RELN superficiali, che e' l'assegnazione standard. Chi porta via da questo paper 'strati profondi su, superficiali giu' lo porta al contrario.\n- **4. Il null SCAR12 e' piu' morbido del testo.** I Risultati riportano nessuna differenza astrocitaria significativa (Fig EV5A/B) e marcatori corticali comparabili (Fig EV4C). La Fig EV5B marca GFAP e ALDH1A1 significativi in un fratello affetto; la Fig EV4C marca SATB2 significativo in entrambi e RELN in uno; e l'Appendix Table S1, per il confronto forebrain che copre, da' GFAP P = 0,0311, S100B P = 0,0237, AQP4 P = 0,0077, ALDH1A1 P = 0,0061. La separazione fra SCAR12 e WOREE in questa piattaforma e' di grado.\n- **5. L'Appendix Table S1 non copre le figure principali.** I Metodi dichiarano che i P-value esatti sono in Appendix Table S1; la tabella distribuita elenca P-value esatti SOLO per le Appendix Figs S2A, S3C, S4E e S5D/F/H/I. Nessun P-value di figura principale o Expanded View e' distribuito da nessuna parte: ogni effect size citato dalle Figg 1-6 ed EV1-EV5 e' letto da un grafico con bande di asterischi.\n- **6. Il rescue GABAergico e' solo proteico.** La Fig 1F riporta GAD67 per nucleo da circa 1,0 (KO) a circa 0,1 nella linea W-AAV (****); la Fig 1D lascia il trascritto GAD1 a circa 7,5 volte il wild type nella STESSA linea (KO circa 8,5 volte). Il testo registra entrambi come 'followed the same trend'.\n- **Una assenza, come osservazione**: il simbolo WWOX non compare in NESSUNA delle due tabelle Expanded View di espressione differenziale (1.246 su, 1.021 giu, entrambe aperte e controllate per appartenenza del simbolo). Un frameshift in esone 1 con codone di stop prematuro ci si attenderebbe mostri decadimento mediato da nonsenso. Il knockout e' evidenziato da immunoblot, non dal trascrittoma pubblicato accanto. E' una osservazione sulle tabelle depositate, non una accusa sul knockout.\n- **Cosa NON fa questo lead**: non ritratta ne' declassa alcun risultato del paper, non tocca DL-MECH-098, DL-THER-105 o PAPER 039, e non afferma che il risultato gamma sia sbagliato - solo che non e' quantificato.\n- **Falsificatore**: la distribuzione, da parte degli autori o dell'editore, di una tabella di P-value esatti per le figure principali ed Expanded View, oppure di una versione corretta dell'EV1J. Finche' non esiste, ogni effect size tratto da questo paper va citato come letto da un pannello.\n- **Not medical advice.**\n"
 }
]
```

## `### LOCATOR TRIPLES FOR BLIND AUDIT`

```
(The Results assert that the 4-AP response was absent in wild type. | the KO line showed significantly increased activity, which was otherwise absent in WT traces | PMID 34268881, Results, "WWOX-depleted cerebral organoids exhibited hyperexcitability and epileptiform activity", para 2; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The panel cited for that claim draws a significance marker on the wild-type comparison too. | [figure attestation] Figure EV1 panel J plots four bars - WT baseline, WT 4-AP, KO baseline, KO 4-AP - at about 0.022, 0.067, 0.072 and 0.100 area-under-curve, with a drawn bracket marked * over the WT pair and a second drawn bracket marked * over the KO pair. | PMID 34268881, Figure EV1 panel J; files/fulltext/PMID34268881_assets/EMMM-13-e13610-g011.jpg)

(The Results assert a decrease in the 30 to 79.9 Hz band. | and a decrease in the 30‐ to 79.9‐Hz high‐frequency range | PMID 34268881, Results, same section, para 1; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(That decrease is marked non-significant in its own quantification. | [figure attestation] Figure EV1 panel H, "30-79.9Hz Range - Week 7 COs", plots WT at about 0.0098 and KO at about 0.0035 with a drawn bracket labelled n.s., over 14 slices in each arm. | PMID 34268881, Figure EV1 panel H; files/fulltext/PMID34268881_assets/EMMM-13-e13610-g011.jpg)

(The Results assign TBR1, BCL11B, SATB2 and POU3F2 to layers I-IV and CUX1 and RELN to superficial layers V-VI. | with layers I‐IV (marked by TBR1, BCL11B, SATB2, POU3F2) showing decreased expression and superficial layers V‐VI (marked by CUX1 and RELN) exhibiting marked increase | PMID 34268881, Results, "RNA-sequencing of WWOX-depleted cerebral organoids revealed major differentiation defects", final paragraph; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The paper's own figure legend orders the same six markers from deepest to most superficial. | from deepest to the most superficial: TBR1, BCL11B (CTIP2), SATB2, POU3F2 (BRN2), CUX1, and RELN | PMID 34268881, Figure 4 legend, panel F; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The Results assert that the SCAR12 forebrain organoids showed no significant astrocytic difference. | immunostaining and qPCR analyses for astrocytic levels did not reveal significant differences | PMID 34268881, Results, "Brain organoids of patient-derived WWOX-related developmental and epileptic encephalopathies", final paragraph; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(That panel carries two drawn significance markers. | [figure attestation] Figure EV5 panel B, "Astrocytic Markers qPCR - Forebrain Organoids - G372R Family", draws a bracket marked * over GFAP for one affected sibling and a second bracket marked * over ALDH1A1 for the same line, against the heterozygous parental lines. | PMID 34268881, Figure EV5 panel B; files/fulltext/PMID34268881_assets/EMMM-13-e13610-g005.jpg)

(Methods state that the exact P-values for the manuscript are given in Appendix Table S1. | Exact P‐values and the specific tests used are stated in Appendix | PMID 34268881, Materials and Methods, "Statistics"; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)

(The distributed Appendix table is titled as the list of exact p-values for the manuscript, and its rows name only Appendix figures - S2A, S3C, S4E and S5D/F/H/I - with no main-figure or Expanded-View row anywhere. | List of exact p-values presented in the manuscript. | PMID 34268881, Appendix (EMMM-13-e13610-s004.docx), table header and first row; files/fulltext/PMID34268881_assets/EMMM-13-e13610-s004.docx)

(The GABAergic rescue holds at protein level and not at transcript level within the same figure. | [figure attestation] Figure 1 panel D plots GAD1 relative expression at about 1 for WT, about 8.5 for KO and about 7.5 for W-AAV, while panel F plots GAD67 surface area per nucleus at about 0.2, about 1.0 and about 0.1 for the same three genotypes with brackets marked **** on both contrasts. | PMID 34268881, Figure 1 panels D and F; files/fulltext/PMID34268881_assets/EMMM-13-e13610-g006.jpg)
```
