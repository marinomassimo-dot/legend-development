# COMMIT CANDIDATE — CC-20261003-C-SLEEP-SUGGESTIVE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 2 2026-10-03, branch `task/sci-C-20261003`.
**context_policy:** `SOURCE_FIRST`; prior knowledge admitted after the first pass by `registry_records.py get --pmid 39952983`.
**Not medical advice.**

## Target

- `research/discovery_ledger_current.md`: **replace-within** `DL-MECH-013` — three qualifications appended
  to its heading line, each anchored in the source.

`DL-MECH-013` currently reads *"WWOX come regolatore di sleep/network-state: bridge umano +
Drosophila funzionale"*, sourced to this paper. The lead is not refuted and its status is not
changed; three of its load-bearing words are bounded.

## Change class

**MINOR** (§ 7) — a research-layer lead gains a qualification. It is **not** MAJOR: no
`consolidated baseline` claim rests on `DL-MECH-013`, and the lead survives with a narrower scope.

## Ordering

`FTR-20261003-39952983-02` must be in the ledger before this record lands.

## What the reading changes about the lead

**1. "bridge umano" is suggestive, by the authors' own statement.** The limitations paragraph
reads: *"Firstly, the WWOX gene did not reach the conventional genome-wide significance level in
the human GWAS results. Secondly, the number of subjects in each cohort was not sufficient for
GWAS."* The lead p-values are 1.11 × 10⁻⁷ and 2.05 × 10⁻⁷ against the conventional 5 × 10⁻⁸
threshold. The reported Bonferroni values in Supplementary Table 1 — `0.0197` and `0.0364` —
imply correction over roughly 1.8 × 10⁵ tests, not the 6.42 million imputed SNVs; the Manhattan
plot's drawn line is at `P = 1.0 × 10⁻⁵`, which the supplement calls *"the preset threshold"*.

**2. No human WWOX expression was measured.** The Results sentence *"The associations between
WWOX expression and sleep parameters are presented in Table 2"* describes a **genotype** table.
The same conflation appears in the Abstract and the Discussion. The two SNVs are **intronic**, no
eQTL is cited, and no RNA or protein is measured in any human in this paper. Any record that
carries "WWOX expression is associated with sleep duration" from this source is carrying a
sentence the paper does not support.

**3. The human effect is an opportunity measure, not a sleep-physiology measure.** Self-aware
sleep duration and time in bed move together and by similar magnitudes in the minor-homozygote
group (−0.209 h and −0.149 h for rs16948804; −0.304 h and −0.260 h for rs4887991, all
`P ≤ 0.01`), while **habitual sleep efficiency** (`P = 0.14`, `0.20`) and the **Epworth Sleepiness
Scale** (`P = 0.69`, `0.58`) do not move at all. Both moving quantities are items from the same
questionnaire. The magnitude is 12–18 minutes.

**4. The fly allele is a strong hypomorph, not a deletion, and has no rescue arm.** Title and
abstract say *"deletion"* and *"loss-of-function"*; Fig 2A measures *Wwox* mRNA at ≈8 % of
control. The phenotype is a **day-to-night redistribution** — daytime sleep ≈500 → ≈300 min
(`****`), night-time ≈560 → ≈650 min (`****`), net ≈−110 min over 24 h — with daytime bout length
down (`**`), night-time bout length unchanged (**n.s.**), and the free-running period and
rhythmicity untouched (≈23.5 h; 96.9 % vs 96.7 % rhythmic). There is **no genetic rescue, no
second allele, no tissue-specific knockdown, one control background, and males only.**

## What survives

The fly phenotype is real, large and automated, and it is a **non-seizure behavioural endpoint**
for *Wwox* loss — which is scarce. The lead keeps that. What it loses is the word "bridge": the
human arm is a suggestive intronic association on a self-reported item in a general adult
population, not a measurement in anyone with a WWOX disorder, and the two arms are not joined by
any measured quantity.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 against `0ed6ad4` (main `eb01d5f` merged))

```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-013",
  "old": "WWOX come regolatore di sleep/network-state: bridge umano + Drosophila funzionale",
  "new": "WWOX come regolatore di sleep/network-state: Drosophila funzionale, braccio umano SOLO SUGGESTIVO ⚠️ (qualificato 2026-10-03, CC-20261003-C-SLEEP-SUGGESTIVE-01, lettura di prima persona FTR-20261003-39952983-02). Tre vincoli, ciascuno ancorato alla sorgente: (a) gli autori dichiarano nelle proprie limitazioni che «the WWOX gene did not reach the conventional genome-wide significance level» e che «the number of subjects in each cohort was not sufficient for GWAS» — i p-value guida sono 1,11e-7 e 2,05e-7 contro la soglia convenzionale di 5e-8, e i valori Bonferroni della Supplementary Table 1 (0,0197 e 0,0364) implicano una correzione su circa 1,8e5 test, non sui 6,42 milioni di SNV imputati, con la linea del Manhattan tracciata a 1e-5; (b) NESSUNA espressione umana di WWOX e' misurata nel paper — le due varianti sono introniche, non e' citato alcun eQTL, e la frase dei Risultati «The associations between WWOX expression and sleep parameters are presented in Table 2» descrive una tabella di GENOTIPI; (c) l'effetto umano si muove con il TEMPO A LETTO e non con la fisiologia del sonno — durata auto-riferita e time in bed calano insieme nel gruppo omozigote minore (-0,209 h e -0,149 h per rs16948804; -0,304 h e -0,260 h per rs4887991, tutti P <= 0,01) mentre efficienza abituale del sonno (P = 0,14 e 0,20) ed Epworth (P = 0,69 e 0,58) non si muovono affatto, e le due quantita' che si muovono sono due voci dello stesso questionario, per 12-18 minuti. Il braccio Drosophila regge e resta il valore del lead, con due precisazioni: l'allele Wwox-f04545 e' un IPOMORFO FORTE (mRNA a circa l'8 per cento del controllo, Fig 2A), non la delezione che titolo e abstract dichiarano; e il fenotipo e' una RIDISTRIBUZIONE giorno-notte — sonno diurno da circa 500 a circa 300 minuti (****), notturno da circa 560 a circa 650 (****), netto circa -110 minuti su 24 h — con bout length diurna giu' (**), notturna invariata (n.s.) e periodo in corsa libera e ritmicita' intatti (circa 23,5 h; 96,9 contro 96,7 per cento ritmici). NON esiste braccio di rescue, ne' secondo allele, ne' knockdown tessuto-specifico; un solo background di controllo e soli maschi"
 }
]
```

## `### LOCATOR TRIPLES FOR BLIND AUDIT`

```
(The authors state in their own limitations that the association does not reach genome-wide significance and that the cohorts were underpowered. | Firstly, the WWOX gene did not reach the conventional genome-wide significance level in the human GWAS results. Secondly, the number of subjects in each cohort was not sufficient for GWAS | PMID 39952983, Discussion, limitations paragraph; files/fulltext/PMID39952983_Kim2025_EPMC.xml)

(The Results label a genotype table as an expression association. | The associations between WWOX expression and sleep parameters are presented in Table | PMID 39952983, Results, "Associations of SNVs with sleep parameters in human GWAS", final paragraph; files/fulltext/PMID39952983_Kim2025_EPMC.xml)

(The human effect moves with time in bed, while sleep efficiency and daytime sleepiness do not move. | presented shorter self-aware sleep duration and time in bed (TIB) than the major homozygous group | PMID 39952983, Results, same paragraph; files/fulltext/PMID39952983_Kim2025_EPMC.xml)

(The fly allele is an insertion line whose transcript is reduced, although the title calls it a deletion. | We first verified that the Wwox mRNA levels in Wwox | PMID 39952983, Results, "Deletion of Wwox reduced daytime sleep quality but increased night-time sleep duration in Drosophila", para 1; files/fulltext/PMID39952983_Kim2025_EPMC.xml)

(The fly phenotype is a day-to-night redistribution on a strong hypomorph, with the circadian clock untouched. | [figure attestation] Figure 2 panel A plots relative Wwox mRNA at 1.0 for the control and about 0.08 for the mutant with a bracket marked ****; panel C plots daytime sleep at about 500 against about 300 minutes and night-time sleep at about 560 against about 650 minutes, both marked ****; panel E plots free-running period at about 23.5 hours for both genotypes with rhythmicity printed as 96.9 and 96.7 percent; panel F marks the daytime bout-length difference ** and the night-time one n.s. | PMID 39952983, Figure 2 panels A, C, E and F; files/figures/PMID39952983/41598_2024_81158_Fig2_HTML.jpg)
```

---

## BATCH DISPOSITION — `BATCH_20261003_001` (2026-10-03, ACTOR_ID `scientist`, Scientist F), append-only

**Verdict:** PROPAGATED

Propagated record-scoped by `BATCH_20261003_001` (2026-10-03, ACTOR_ID `scientist`, Scientist F) — the ops below were read from this file by script, never retyped; every byte outside the addressed records was proven unchanged before anything was written. Post-propagation LINT: WARN, 0 BLOCK.

`discovery_ledger_current.md`, 1 op on `DL-MECH-013`. The lead keeps its *Drosophila* value and loses the word *bridge*; status unchanged.
