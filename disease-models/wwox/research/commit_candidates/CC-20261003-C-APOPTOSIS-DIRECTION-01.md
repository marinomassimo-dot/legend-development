# COMMIT CANDIDATE — CC-20261003-C-APOPTOSIS-DIRECTION-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist C), intake wave 2 2026-10-03, branch `task/sci-C-20261003`.
**context_policy:** `SOURCE_FIRST` for all readings; comparison with LEGEND's records made after each first pass.
**Not medical advice.**

## Target

- `research/discovery_ledger_current.md`: **create** one lead, provisionally `DL-THER-115`.
- `research/discovery_ledger_current.md`: **replace-within** `DL-MECH-023` — one appended sentence
  recording that the inhibitor panel the lead rests on carries no statistics and that the KIRA6
  increment is the same in both genotypes.

**Numbers are provisional.** The integrator renumbers in event order.

## Change class

**MINOR** (§ 7). No `consolidated baseline` claim is narrowed or reversed; `DL-MECH-023` is a
research-layer lead and gains a qualification, not a status change.

## Ordering

The receipts `FTR-20261003-26302329-01`, `FTR-20261003-28749468-01` and
`FTR-20261003-34268881-06` must be in the ledger before this record lands.

## The finding — one direction, three organisms

Three independent systems, read first-hand in this group, agree on the **sign** of WWOX's effect
on stress-induced apoptosis. Nothing in the corpus had put them beside each other.

| System | Manipulation | Direction |
|---|---|---|
| Human WWOX-null cerebral organoids, ventricular zone (PMID 34268881, Fig EV2G/H) | CRISPR exon-1 null, then AAVS1 restoration | Cleaved caspase-3 per SOX2⁺ cell falls from ≈24 % to ≈9 % on loss (`**`) and returns to ≈16 % on restoration (`*` vs KO, n.s. vs WT) |
| *Drosophila* eye and wing disc under ectopic Egr/TNFα (PMID 26302329, Figs 1D, 1F; S1 Fig F) | two RNAi lines, two heterozygous null alleles, two overexpression constructs | Loss **protects**: eye area rises from 25 to 31.5–34.5 ×10⁴ px (`****`); a single heterozygous allele already shifts it (`*`, `****`). Gain **worsens** it (cDNA, `*`) |
| Human *WWOX*-null ovarian carcinoma line PEO1 (PMID 28749468, Figs 1a, 2a, 4c) | stable WWOX restoration, then siRNA removal | Restoration roughly halves survival under paclitaxel (0.32–0.38 → 0.17–0.19, `**`) and tunicamycin (0.63 → 0.31, `***`); removal roughly doubles it |

**Statement:** `WWOX loss lowers the stress-induced apoptotic response; WWOX restoration raises
apoptotic sensitivity under stress.` `DATO` in each system for its own endpoint; `INFERENZA` as a
cross-species direction; `IPOTESI` for any neuron of the reference genotype class.

## Why this matters, stated without overreach

A WWOX gene-replacement strategy aims to restore protein in neurons that are already stressed —
by a DNA-damage load that PMID 34268881 measures directly in the ventricular zone (γH2AX 0.78 →
1.5 foci per nucleus), and by whatever metabolic and oxidative load the disorder imposes. The three
systems above say that the restored state is the **more apoptosis-competent** state. In the
organoid that is read as a *correction* — checkpoint function returning toward wild type. In the
fly and the carcinoma line the same direction is read as *death*.

This is a **dose-and-context question for the therapeutic layer**, not a reason to abandon
replacement, and this candidate does not propose one. Two facts bound it:

* In the organoid the restored value (≈16 %) is **not significantly different from wild type**,
  so within that system the restoration normalises rather than overshoots on this endpoint.
* In the fly, **ectopic WWOX alone produces no phenotype at all** — the effect appears only when
  a stressor is co-expressed.

What is missing, and what would settle it, is a titrated restoration in stressed human neurons
with apoptosis as a declared endpoint. No source in this group provides it.

## Caveats carried with the lead

* The *Drosophila* result's only supporting quantification, Fig 5G, is **labelled in the opposite
  sense to its own text, legend and panel labels** (see `research/fulltext_dossiers/PMID26302329.md`
  § 6). The eye-area series (Fig 1D/1F, S1 Fig F) is unaffected and is the one carrying the
  direction here.
* The ovarian paper's central IRE-1 claim is weaker than stated: Figures 5c–5e carry **no
  significance markers at all**, and the absolute viability increment from KIRA6 is the same in
  the WWOX-expressing and WWOX-null clones (≈0.19 against ≈0.18), so the "blunted effect" is a
  fold-change artefact of the lower baseline.
* The *Drosophila* complete null is **viable to adulthood**, so this organism does not reproduce
  the severity of human biallelic WWOX loss.
* PEO1 is a cancer line whose stressor is a chemotherapeutic. Nothing here is a neuron.

## Related integrity note

`dependency_integrity.py screen` returns **`FLAGGED_RETRACTION`** for PMID 26302329 on two
citation-only dependencies, one of which is **Fabbri 2005 (`10.1073/pnas.0505485102`, PMID
16223882), under an expression of concern since 2017**. That paper is a load-bearing citation for
the general premise that *WWOX restoration suppresses tumour growth in vivo*. It supplies nothing
to PMID 26302329 itself, and this candidate proposes no action on it — it is recorded because any
future record that leans on "WWOX restoration works in vivo" should know which source carries it.

## Op list — `discovery_ledger_current.md` (record-scoped; dry run 2026-10-03 against `0ed6ad4` (main `eb01d5f` merged))

```json
[
 {
  "op": "append",
  "text": "\n### DL-THER-115 — Tre organismi, una direzione: il restauro di WWOX ALZA la sensibilita apoptotica sotto stress\n\n- **Status**: open · **Tag**: DATO per singolo sistema, INFERENZA come direzione cross-specie, IPOTESI per il neurone del genotipo di riferimento · **Fonte**: intake wave 2 2026-10-03, Scientist C — PMID 34268881 (Fig EV2G/H), PMID 26302329 (Figs 1D, 1F, S1 Fig F), PMID 28749468 (Figs 1a, 2a, 4c), tutti letti in prima persona con i pannelli ispezionati.\n- **Causal statement**: in tre sistemi indipendenti la perdita di WWOX ABBASSA la risposta apoptotica indotta da stress e il restauro di WWOX la RIALZA. Organoidi cerebrali umani WWOX-null: caspasi-3 clivata per cellula SOX2+ nella zona ventricolare da circa 24 per cento (WT) a circa 9 per cento (KO, **) e ritorno a circa 16 per cento col restauro AAVS1 (* contro KO, n.s. contro WT). Drosophila sotto Egr/TNFalpha ectopico: la riduzione di WWOX PROTEGGE - area dell'occhio da 25 a 31,5-34,5 per diecimila pixel con due linee RNAi indipendenti (****), e un SINGOLO allele eterozigote di perdita di funzione sposta gia' l'endpoint (* e ****) - mentre l'aumento di WWOX peggiora il fenotipo (costrutto cDNA, *). Linea di carcinoma ovarico umano PEO1, WWOX-null per delezione omozigote degli esoni 4-8: il restauro dimezza circa la sopravvivenza sotto paclitaxel (0,32-0,38 a 0,17-0,19, **) e sotto tunicamicina (0,63 a 0,31, ***); la rimozione la raddoppia circa.\n- **Perche' conta**: una strategia di sostituzione genica restituisce proteina a neuroni GIA' sotto stress - PMID 34268881 misura direttamente un carico di danno al DNA nella zona ventricolare, gamma-H2AX da 0,78 a 1,5 foci per nucleo. Questi tre sistemi dicono che lo stato restaurato e' lo stato PIU' competente all'apoptosi. Nell'organoide la stessa direzione si legge come correzione del checkpoint; nella mosca e nella linea tumorale si legge come morte. E' una questione di DOSE e CONTESTO per il layer terapeutico, non un argomento contro la sostituzione.\n- **Cio' che limita l'allarme**: nell'organoide il valore restaurato (circa 16 per cento) NON e' significativamente diverso dal wild type, quindi in quel sistema il restauro normalizza e non supera; e nella mosca l'espressione ectopica di WWOX DA SOLA non produce alcun fenotipo - l'effetto compare solo in presenza di uno stressore.\n- **Counter-evidence e difetti di sorgente**: l'unica quantificazione a sostegno del risultato caspasi-3 in Drosophila, Fig 5G, e' etichettata in senso OPPOSTO al proprio testo, alla propria didascalia e alle etichette dei pannelli sopra di essa (dettaglio in research/fulltext_dossiers/PMID26302329.md); la serie dell'area oculare non ne e' toccata ed e' quella che porta la direzione qui. Nel paper ovarico le Figure 5c-5e, che portano la tesi centrale su IRE-1, non recano alcun marcatore di significativita' e l'incremento assoluto di vitalita' prodotto da KIRA6 e' identico nei due genotipi (circa 0,19 contro circa 0,18), quindi l'attenuazione dichiarata e' un artefatto di fold-change sulla baseline piu' bassa. Il null completo di Drosophila e' VITALE in eta' adulta. PEO1 e' una linea tumorale e lo stressore e' un chemioterapico: nessuno di questi sistemi contiene un neurone.\n- **Esperimento che lo discrimina**: restauro titolato di WWOX in neuroni umani derivati da paziente sotto uno stressore dichiarato, con l'apoptosi come endpoint dichiarato e un comparatore wild type a ogni dose. Se la sensibilita' apoptotica cresce in modo monotono con la dose di WWOX oltre il livello wild type, la direzione diventa un vincolo di dose; se satura al livello wild type, non lo e'.\n- **Nota di integrita'**: dependency_integrity.py screen restituisce FLAGGED_RETRACTION per PMID 26302329 su due dipendenze di sola citazione. Una e' Fabbri 2005 (10.1073/pnas.0505485102, PMID 16223882), sotto expression of concern dal 2017, che e' una citazione portante per la premessa generale secondo cui il restauro di WWOX sopprime la crescita tumorale in vivo. Non fornisce nulla a PMID 26302329; e' registrata qui perche' qualunque record futuro che si appoggi a quella premessa sappia da quale sorgente viene.\n- **Not medical advice.**\n"
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-023",
  "old": "WWOX orienta UPR adattativa-vs-terminale sotto stress ER",
  "new": "WWOX orienta UPR adattativa-vs-terminale sotto stress ER ⚠️ (qualificato 2026-10-03, CC-20261003-C-APOPTOSIS-DIRECTION-01: le Figure 5c-5e di Janczar 2017, che portano la tesi su IRE-1, non recano alcun marcatore di significativita', e l'incremento assoluto di vitalita' prodotto da KIRA6 e' lo stesso nel clone WWOX-positivo e in quello WWOX-null — circa 0,19 contro circa 0,18 — quindi l'attenuazione dichiarata e' un artefatto di fold-change; il paper afferma inoltre esplicitamente che l'attivazione di PERK non cambia con lo stato di WWOX)"
 }
]
```

## `### LOCATOR TRIPLES FOR BLIND AUDIT`

```
(In the Drosophila model, reducing WWOX suppresses the TNF-alpha-induced phenotype rather than worsening it. | resulted in suppression of the Egr/TNF | PMID 26302329, Results, "Altered WWOX modulates ectopic Egr/TNFalpha eye phenotypes", para 1; files/fulltext/PMID26302329_OKeefe2015_PMC.xml)

(Ectopic WWOX on its own produces no phenotype; the modulation appears only under stress. | Ectopic expression of WWOX alone does not result in any obvious cell death-induced phenotype | PMID 26302329, Results, "Altered WWOX modulates ectopic Egr/TNFalpha eye phenotypes", para 2; files/fulltext/PMID26302329_OKeefe2015_PMC.xml)

(A single heterozygous loss-of-function allele already shifts the endpoint, and the empty-vector lane carries essentially no detectable Wwox. | [figure attestation] Supplementary Figure 1 panel F plots wild type, WWOX1/+ and WWOX2/+ at about 26, 29 and 32 times ten to the fourth pixels with brackets marked * and ****; panel I shows the empty-vector lane at essentially zero Wwox/Tubulin signal while the ORF and cDNA lanes sit at about 0.33 and 0.35. | PMID 26302329, Supplementary Figure 1 panels F and I; files/fulltext/PMID26302329_assets/pone.0136356.s001.tif)

(A complete Drosophila WWOX null is viable to adulthood. | or where WWOX function is completely removed (trans-heterozygous for independent WWOX alleles) | PMID 26302329, Results, "Requirement for WWOX tumor suppressor activity in vivo", final paragraph; files/fulltext/PMID26302329_OKeefe2015_PMC.xml)

(The gain-of-function host line is a human WWOX-null by homozygous deletion of exons 4 to 8. | is homozygously deleted for WWOX exons 4 | PMID 28749468, Materials and methods, "Cell lines"; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(Restoring WWOX increases death under ER stress and removing it increases survival. | whereas WWOX siRNA knockdown increased survival | PMID 28749468, Results, "Paclitaxel induces ER stress response and WWOX determines cell fate in response to prolonged ER stress", para 1; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(The paper states that PERK activation is unchanged by WWOX status. | No changes in activation of PERK were observed as a result of WWOX status | PMID 28749468, Results, same section, para 2; files/fulltext/PMID28749468_Janczar2017_PMC.xml)

(The inhibitor panels that carry the central IRE-1 claim print no significance marker, and the KIRA6 increment is the same in both genotypes. | [figure attestation] Figure 5 panels c, d and e carry grouped bars with error bars and no asterisk, bracket or P-value of any kind. In panel c the WWOX-8 bars read about 0.05 for paclitaxel alone and about 0.24 for paclitaxel plus KIRA6, while the Vector-9 bars read about 0.13 and about 0.31. | PMID 28749468, Figure 5 panels c-e; files/fulltext/PMID28749468_assets/cddis2017346f5.jpg)

(Apoptosis in the ventricular zone falls on WWOX loss and returns toward wild type on restoration. | which revealed a decline in apoptosis of these cells upon WWOX‐KO, and was rescued in the W‐AAV COs | PMID 34268881, Results, "WWOX-depleted cerebral organoids exhibited impaired astrogenesis and DNA damage response", final para; files/fulltext/PMID34268881_Steinberg2021_PMC.xml)
```
