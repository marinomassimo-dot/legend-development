"""ADV-244 wording, second increment (IT, 2026-11-25): (a) the batch limit, sourced (PMID 34268881 Methods 'For all analyses, organoids from the same batch were used, unless stated otherwise';
authors' reply, peer-review file p. 24: 'a totally different batch of the one we performed the RNA-seq'), in the six placed packets and INV-16; (b) the same carried limit in the packets of E01, E03 and F01.
Text-level, idempotent; cards are rebuilt by repurposing_bridge.py afterwards. Run from the repository root. Hypothesis level; nothing is medical advice."""
import importlib.util, json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("a1", DR / "advisor_pilot_20261113/brainstorm_20261116/it_adv244wording_20261125/apply_adv244_wording_it_20261125.py")
a1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(a1)
OLD_NK = a1.NK; OLD_INV = a1.INV
NEW_NK = ("Whether any organoid transcript difference or null on this card (deposit GSE156243) is independent of the CRISPR clone and of the batch: the sequenced knockout organoids are four "
          "of ONE clone (1B, from edit-spanning reads, ADV-244, SCI, 2026-11-25), the other clone (A2) was not sequenced, the comparator is two organoids of the parental line "
          "(the authors removed two of four wild-type libraries, one for failed quality control and one for not clustering), and the organoids appear to come from one batch "
          "(the authors' Methods: organoids from the same batch were used for all analyses unless stated otherwise; their reply to reviewers speaks of the batch of the RNA-seq; "
          "not stated as a measured fact for these six libraries), so a difference here is not shown to be a property of the knockout rather than of the clone or the batch. [IT 2026-11-25, ADV-244]")
NEW_INV = (" [IT 2026-11-25, ADV-244: the human organoid transcript set is four knockout organoids of one CRISPR clone (1B) against two parental organoids, apparently from one batch "
           "(authors' Methods: organoids from the same batch unless stated otherwise), so 'higher in the organoid' is not shown to be independent of the clone; the other clone was not sequenced.]")
SIX = a1.CARDS; THREE = ["E01_isr_modulators", "E03_pdk_inhibition_dca", "F01_glutamate_receptor_node"]
def j(s): return json.dumps(s, ensure_ascii=False)[1:-1]
def packets():
    n = 0
    for c in SIX:
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8")
        if j(OLD_NK) in raw:
            raw = raw.replace(j(OLD_NK), j(NEW_NK)); json.loads(raw); p.write_text(raw, encoding="utf-8"); n += 1
    for c in THREE:
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8")
        if j(NEW_NK) in raw: continue
        d = json.loads(raw); old = json.dumps(d["not_known"][-1], ensure_ascii=False)
        i = raw.index(old, raw.index('"not_known"')); k = raw.rindex("\n", 0, i) + 1; ind = raw[k:i]; assert ind.strip() == ""
        raw = raw[:i + len(old)] + ",\n" + ind + json.dumps(NEW_NK, ensure_ascii=False) + raw[i + len(old):]
        json.loads(raw); p.write_text(raw, encoding="utf-8"); n += 1
    return n
def inv():
    RK = DR / "ranking_it8_p9_20261029"; n = 0
    for f in ("investigations.tsv", "investigations_it20.tsv", "ranking.json"):
        p = RK / f; raw = p.read_text(encoding="utf-8")
        o = j(OLD_INV) if f.endswith("json") else OLD_INV
        nw = j(NEW_INV) if f.endswith("json") else NEW_INV
        if o in raw: p.write_text(raw.replace(o, nw), encoding="utf-8"); n += 1
    return n
if __name__ == "__main__":
    print("packets", packets(), "inv files", inv())
