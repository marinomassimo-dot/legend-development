"""ADV-255 lactate wording (IT, 2026-11-25; SCI's section 2 of the lactate table and ADV-259, relayed by SCI at ADV's request): E02 and E04 packets (evidence_against, not_known), text-level and idempotent;
cards are rebuilt by repurposing_bridge.py afterwards. Run from the repository root. Hypothesis level; nothing is medical advice."""
import json
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
M = " [IT 2026-11-25, ADV-255 via SCI]"
NEW_AGAINST = ("Human lactate in WWOX deficiency: blood normal where stated (5 publications, up to 14 subjects, no values printed); spectroscopy mixed (one report with small peaks in early infancy "
               "and none later, one report 'extremely low', confounded by a second candidate variant); one raised value in the registry is without a held source passage." + M)
EDITS = {
    "E02_ldh_inhibition": [("evidence_against", "Human lactate in WWOX deficiency reported normal or extremely low.", NEW_AGAINST)],
    "E04_ketogenic_lactate_axis": [
        ("evidence_against", "Four sources report normal human metabolism in WWOX deficiency (DL-BIO-009); one MRS report has lactate extremely low (DL-BIO-008).", NEW_AGAINST + " The earlier 'four sources' count was withdrawn on 2026-10-27."),
        ("not_known", "(lactate 2.4 to 3.3 mmol/L in one individual)", "(lactate 2.4 to 3.3 mmol/L in one individual; registry statement, no held source passage, ADV-259)"),
    ],
}
def main():
    n = 0
    for c, edits in EDITS.items():
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8")
        for field, old, new in edits:
            jo = json.dumps(old, ensure_ascii=False)[1:-1]; jn = json.dumps(new, ensure_ascii=False)[1:-1]
            if jn in raw: continue
            assert raw.count(jo) == 1, (c, old[:50], raw.count(jo))
            raw = raw.replace(jo, jn); n += 1
        json.loads(raw); p.write_text(raw, encoding="utf-8")
    return n
if __name__ == "__main__":
    print("edits", main())
