"""Denominators in the FDA 2018 review, Table 14. Percentage changes as printed."""
rows = [
    (25.3, -13.8, 72.6), (50.0, -30.8, 27.6), (11.8, 62.4, -100.0),
    (0.0, 36.0, -73.6), (-40.0, 57.2, -100.0),
]
print("selection\tpatients\tseizure_reduction_at_least_half")
selections = {
    "FDA_displayed": rows,
    "strict_printed_thresholds": [r for r in rows if r[0] < 50 and r[1] < 100],
    "neither_companion_increased": [r for r in rows if r[0] <= 0 and r[1] <= 0],
}
for name, selected in selections.items():
    print(name, len(selected), sum(r[2] <= -50 for r in selected), sep="\t")
