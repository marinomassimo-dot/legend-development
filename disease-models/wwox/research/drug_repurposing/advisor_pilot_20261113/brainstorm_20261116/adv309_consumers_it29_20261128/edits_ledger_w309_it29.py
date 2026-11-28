# Exact-once fragments for DL-MECH-027 (W3). Run: python3 edits_ledger.py check|apply  from the repo root.
X = [{'path': 'disease-models/wwox/research/discovery_ledger_current.md', 'tag': 'W3-title', 'old': '### DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile\n- **Status**: open · **Tag**: DATO (ratto)', 'new': '### DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)\n- **Status**: open · **Tag**: DATO (ratto)'}, {'path': 'disease-models/wwox/research/discovery_ledger_current.md', 'tag': 'W3-body', 'old': 'È esattamente il tipo di danno su cui una leva di protezione-finestra può mordere.', 'new': 'È il tipo di danno su cui una leva di protezione-finestra **potrebbe** agire: **ipotesi, non risultato** — nel ratto non è testato alcun rescue, alcuna reversibilità né alcuna età di intervento (solo osservazione a PND 5-21; cfr. `DL-MECH-071`).'}, {'path': 'disease-models/wwox/research/discovery_ledger_current.md', 'tag': 'W3-anchor-1 (follows the heading; line ~765)', 'old': '[[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]]', 'new': '[[meta_network_myelin_glia_current]], [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)|DL-MECH-027]]'}, {'path': 'disease-models/wwox/research/discovery_ledger_current.md', 'tag': 'W3-anchor-2 (follows the heading; line ~1055)', 'old': '**mutante instabile sfuggito alla degradazione** ([[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]]', 'new': '**mutante instabile sfuggito alla degradazione** ([[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)|DL-MECH-027]]'}, {'path': 'disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md', 'tag': 'W3-anchor-3 (other file; follows the heading; line ~293)', 'old': '**Evidenza PRO:** [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile|DL-MECH-027]]', 'new': '**Evidenza PRO:** [[discovery_ledger_current#DL-MECH-027 — Nel *lde*: ipomielinizzazione con oligodendrociti maturi ridotti e **neuroni intatti**. Il substrato è salvabile (ipotesi; nessun rescue testato; PND 5-21)|DL-MECH-027]]'}]

if __name__ == "__main__":
    import sys, pathlib
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    root = pathlib.Path(".")
    bad = 0
    texts = {}
    for e in X:
        p = root / e["path"]
        t = texts.setdefault(e["path"], p.read_text(encoding="utf-8"))
        n = t.count(e["old"])
        print(f'{e["tag"]}: old occurs {n}x in {e["path"]}')
        if n != 1:
            bad += 1
    if mode == "apply" and not bad:
        for e in X:
            texts[e["path"]] = texts[e["path"]].replace(e["old"], e["new"], 1)
        for path, t in texts.items():
            (root / path).write_text(t, encoding="utf-8")
        print("applied")
    sys.exit(1 if bad else 0)
