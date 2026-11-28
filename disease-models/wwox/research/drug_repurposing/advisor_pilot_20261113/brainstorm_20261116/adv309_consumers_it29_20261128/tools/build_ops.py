import json, pathlib
W = pathlib.Path("/home/desktop/.claude/jobs/c6caa74e/tmp/w309")

# ---------------- CLAIM 036 (W1) ----------------
T036_OLD = "so any brain phenotype measured in that window carries"
T036_NEW = "so any brain phenotype measured at P18 in this EIIA-Cre line carries"

CM036_OLD = ("qualunque fenotipo ippocampale o cerebrale misurato in un null **sistemico** nella finestra P14–P18 "
             "è misurato in un animale simultaneamente ipoglicemico, acidotico, uremico e anemico.")
CM036_NEW = ("qualunque fenotipo ippocampale o cerebrale misurato a P18 in un null **sistemico** della linea EIIA-Cre "
             "è misurato in un animale con glucosio ridotto (143.5 vs 250.6 mg/dL), BUN raddoppiato (37.25 vs 17.67 mg/dL) "
             "e CO₂ totale ridotta (14.50 vs 21.67 mEq/L) — valori che gli autori leggono come compatibili con insufficienza renale "
             "e acidosi metabolica, ma senza pH né creatinina misurati — e con leucopenia e segni di anemia (WBC 4.2 vs 9.45 ×10³/µL, "
             "`n=2/gruppo`, età della conta non dichiarata; eritrociti nucleati al 3% in uno solo dei due topi KO esaminati; "
             "nessun emocromo). La chimica ematica (`n=3/3/4`) esiste solo a P18: a P14 l'unica misura è il peso corporeo "
             "(4.2 g contro 6.82 e 7.07 g), e per i topi KO BK5-Cre di due settimane di PMID 30290271 non esiste alcuna chimica ematica, "
             "quindi lo stesso confondente è lì una possibilità, non una misura.")

IM036_OLD = "i null sistemici nella finestra P14–P18 non separano cell-autonomo da sistemico."
IM036_NEW = "il null sistemico EIIA-Cre a P18, l'unica età con chimica ematica, non separa cell-autonomo da sistemico."

# ---------------- CLAIM 014 (W2) ----------------
S014_OLD = "defective cortical maturation with downstream hypomyelination/glial-development abnormalities."
S014_NEW = (S014_OLD + " (Ages and tissues sampled: Iacomino 2020 — one WWOX-deficient human fetus at 21 gestational weeks, "
            "lde/lde rat brain at P1 with BrdU given at E16.5 and traced to P1, and human neural progenitor cells in vitro "
            "(a re-analysis of the Kośla 2019 deposit); Tochigi 2019 — hypomyelination and reduced cortical GFAP and Iba1 "
            "in lde/lde rat cortex at PND 5 to 21 only; Kośla 2019 — human neural progenitor cells in vitro, no animal or fetal age.)")

# ---------------- CLAIM 005 (W4) ----------------
G005_OLD = "segnale GABAergico e gliale plausibilmente trasferibile come meccanismo generale di vulnerabilità"
G005_NEW = ("segnale GABAergico e gliale misurato nell'ippocampo del topo KO sistemico (linea BK5-Cre) a due settimane di età, "
            "in un solo studio (PMID 30290271); la trasferibilità come meccanismo generale di vulnerabilità resta un'ipotesi plausibile "
            "ma non dimostrata — stadio e regione non generalizzati, e nella corteccia del ratto *lde* a PND 5-21 (PMID 31340538) "
            "GFAP e Iba1 sono ridotti, non aumentati")

ops = [
 {"op":"replace-within","id":"CLAIM 036","old":T036_OLD,"new":T036_NEW},
 {"op":"replace-within","id":"CLAIM 036","old":CM036_OLD,"new":CM036_NEW},
 {"op":"replace-within","id":"CLAIM 036","old":IM036_OLD,"new":IM036_NEW},
 {"op":"replace-within","id":"CLAIM 014","old":S014_OLD,"new":S014_NEW},
 {"op":"replace-within","id":"CLAIM 005","old":G005_OLD,"new":G005_NEW},
]
(W/"ops_claims.json").write_text(json.dumps(ops, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------- DL-MECH-027 (W3) ----------------
LP = "disease-models/wwox/research/discovery_ledger_current.md"
TP = "disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md"
H_OLD = "DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile"
H_NEW = H_OLD + " (ipotesi; nessun rescue testato; PND 5-21)"
X = [
 {"path":LP, "tag":"W3-title",
  "old":"### "+H_OLD+"\n- **Status**: open · **Tag**: DATO (ratto)",
  "new":"### "+H_NEW+"\n- **Status**: open · **Tag**: DATO (ratto)"},
 {"path":LP, "tag":"W3-body",
  "old":"È esattamente il tipo di danno su cui una leva di protezione-finestra può mordere.",
  "new":("È il tipo di danno su cui una leva di protezione-finestra **potrebbe** agire: **ipotesi, non risultato** — nel ratto "
         "non è testato alcun rescue, alcuna reversibilità né alcuna età di intervento (solo osservazione a PND 5-21; cfr. `DL-MECH-071`).")},
 {"path":LP, "tag":"W3-anchor-1 (follows the heading; line ~765)",
  "old":"[[meta_network_myelin_glia_current]], [[discovery_ledger_current#"+H_OLD+"|DL-MECH-027]]",
  "new":"[[meta_network_myelin_glia_current]], [[discovery_ledger_current#"+H_NEW+"|DL-MECH-027]]"},
 {"path":LP, "tag":"W3-anchor-2 (follows the heading; line ~1055)",
  "old":"**mutante instabile sfuggito alla degradazione** ([[discovery_ledger_current#"+H_OLD+"|DL-MECH-027]]",
  "new":"**mutante instabile sfuggito alla degradazione** ([[discovery_ledger_current#"+H_NEW+"|DL-MECH-027]]"},
 {"path":TP, "tag":"W3-anchor-3 (other file; follows the heading; line ~293)",
  "old":"**Evidenza PRO:** [[discovery_ledger_current#"+H_OLD+"|DL-MECH-027]]",
  "new":"**Evidenza PRO:** [[discovery_ledger_current#"+H_NEW+"|DL-MECH-027]]"},
]
src = "# Exact-once fragments for DL-MECH-027 (W3). Run: python3 edits_ledger.py check|apply  from the repo root.\nX = " + repr(X) + "\n"
(W/"edits_ledger.py").write_text(src, encoding="utf-8")
print("ok")
