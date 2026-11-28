# Blind check: sentences on age, line and tissue against whole sources

You see only the sentences below and the whole sources in `/home/desktop/.claude/jobs/c6caa74e/tmp/w309/src/`.
Check each sentence against those sources only (no web, no repository, no memory of other papers). For every
sentence give one verdict: KEEP, MUST CHANGE (say what the source says instead, with a short verbatim quote and
where it sits) or OPTIONAL (true but could be tighter). Check every number, age, n, strain/Cre line, tissue and
every absolute or negative word ("only", "no", "none", "one", "not measured") against the WHOLE source, not the
passage that first seems to answer. A negative ("no chemistry exists", "age not reported") is true only if the whole
source is silent; say what you searched. Where a number is printed in a table, read the table cell. Pointers to other record numbers (for example a `DL-MECH` number) cannot be checked here: ignore them. Write your
report to `/home/desktop/.claude/jobs/c6caa74e/tmp/w309/BLIND_REPORT.md`.

## Which source belongs to which sentence

| Sentence | Source files (in the src folder) |
|---|---|
| A1, A2, A3 | `p19936220.txt` (mouse EIIA-Cre line, necropsy and blood chemistry); `p30290271.txt` (two-week BK5-Cre mice) |
| B1 | `p32581702.txt`; `p31340538.txt`; `p31543760.txt` |
| C1, C2 | `p31340538.txt` |
| D1 | `p30290271.txt`; `p31340538.txt` |

## Sentences

**A1** (a title)
> A systemic constitutive Wwox-null mouse at P18 is metabolically decompensated, so any brain phenotype measured at P18 in this EIIA-Cre line carries a quantified systemic confounder

**A2** (a clinical-meaning sentence, in Italian)
> qualunque fenotipo ippocampale o cerebrale misurato a P18 in un null **sistemico** della linea EIIA-Cre è misurato in un animale con glucosio ridotto (143.5 vs 250.6 mg/dL), BUN raddoppiato (37.25 vs 17.67 mg/dL) e CO₂ totale ridotta (14.50 vs 21.67 mEq/L) — valori che gli autori leggono come compatibili con insufficienza renale e acidosi metabolica, ma senza pH né creatinina misurati — e con leucopenia e segni di anemia (WBC 4.2 vs 9.45 ×10³/µL, `n=2/gruppo`, età della conta non dichiarata; eritrociti nucleati al 3% in uno solo dei due topi KO esaminati; nessun emocromo). La chimica ematica (`n=3/3/4`) esiste solo a P18: a P14 l'unica misura è il peso corporeo (4.2 g contro 6.82 e 7.07 g), e per i topi KO BK5-Cre di due settimane di PMID 30290271 non esiste alcuna chimica ematica, quindi lo stesso confondente è lì una possibilità, non una misura.

**A3** (a closing line, in Italian)
> il null sistemico EIIA-Cre a P18, l'unica età con chimica ematica, non separa cell-autonomo da sistemico.

**B1** (an addendum to a summary that says WWOX loss perturbs cortical development, neuronal migration and cortical maturation across fetal human tissue, rat and human neural progenitor models, with downstream hypomyelination and glial abnormalities)
> (Ages and tissues sampled: Iacomino 2020 — one WWOX-deficient human fetus at 21 gestational weeks, lde/lde rat brain at P1 with BrdU given at E16.5 and traced to P1, and human neural progenitor cells in vitro (a re-analysis of the Kośla 2019 deposit); Tochigi 2019 — hypomyelination and reduced cortical GFAP and Iba1 in lde/lde rat cortex at PND 5 to 21 only; Kośla 2019 — human neural progenitor cells in vitro, no animal or fetal age.)

**C1** (a record heading, in Italian)
> DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)

**C2** (a body sentence, in Italian)
> È il tipo di danno su cui una leva di protezione-finestra **potrebbe** agire: **ipotesi, non risultato** — nel ratto non è testato alcun rescue, alcuna reversibilità né alcuna età di intervento (solo osservazione a PND 5-21; cfr. `DL-MECH-071`).

**D1** (a model-relevance phrase, in Italian)
> segnale GABAergico e gliale misurato nell'ippocampo del topo KO sistemico (linea BK5-Cre) a due settimane di età, in un solo studio (PMID 30290271); la trasferibilità come meccanismo generale di vulnerabilità resta un'ipotesi plausibile ma non dimostrata — stadio e regione non generalizzati, e nella corteccia del ratto *lde* a PND 5-21 (PMID 31340538) GFAP e Iba1 sono ridotti, non aumentati
