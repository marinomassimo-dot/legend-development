# Cell-by-cell comparison of the ADV-320 delegate table (D) and HE's ADV-323 blind table (H), Chornyy 2025 (PMID 41036104).
# Values typed from BLIND_FIGURES_CHORNYY2025_ADV320_DELEGATE.md (sections 3 and 7) and BLIND_READING.md (sections 1 and 3).
# A range in H or D is (lo, hi); a distance of 0 means the point lies inside the other reader's range.
def dist(d, h):
    lo_d, hi_d = (d, d) if not isinstance(d, tuple) else d
    lo_h, hi_h = (h, h) if not isinstance(h, tuple) else h
    return max(0.0, lo_d - hi_h, lo_h - hi_d)
STATS = ("Q1", "median", "Q3", "whisker_min", "whisker_max")
pct = {  # promoter: (D, H) over STATS; None = not given by that reader
 "CAG": ((21.5,38.7,42.2,19.5,42.3), (21.6,38.7,42.1,19.5,42.2)),
 "p546": ((10.3,23.2,33.3,7.9,41.9), (10.3,23.3,33.2,7.9,41.8)),
 "GFAP": ((11,17.2,18.5,8.3,24), (11.0,17.1,18.4,8.5,24.0)),
 "gfa1405": ((22.7,26.5,29.2,18.8,35.3), (22.9,26.5,29.1,18.8,35.4)),
 "gfaABC(1)D": ((4.5,5.2,6.3,3.5,9.5), ((3.5,4.0),5.0,6.2,3.5,9.4)),
 "CNP": ((15.2,None,30.1,13,37.2), (15.2,16.8,30.0,13.3,37.2)),
 "tCAG": ((None,1,None,None,(0,3)), ((0.3,0.3),(0.8,1.4),1.4,(0,0.4),3.1)),
 "EFS": ((5,6,8,None,16.4), (4.7,5.4,7.9,1.3,16.4)),
 "MAG": ((4.3,5,5.4,None,None), (4.0,4.9,5.5,4.0,5.6)),
 "rMBP": ((0.8,1.6,3.8,None,4.3), ((0.4,0.8),1.7,4.0,(0.4,0.4),4.3)),
 "Control": ((None,0.3,None,None,None), ((0.1,0.1),(0.3,0.3),(0.5,0.5),0.1,0.6)),
}
rfu = {
 "CAG": ((189,572,661,133,911), (187,578,664,136,913)),
 "p546": ((53,128,286,39,447), (51,124,285,38,447)),
 "GFAP": ((239,408,547,39,792), (242,413,550,41,794)),
 "gfa1405": ((303,461,511,206,694), (306,464,510,207,695)),
 "gfaABC(1)D": ((78,None,128,None,219), (77,(98,104),124,(43,50),220)),
 "CNP": ((20,None,97,None,122), (21,61,98,(0,10),120)),
}
s1b = {  # EGFP/GAPDH x100, mean bar top (D, H)
 "liver p546": (5,5.4), "liver gfa1405": (81,80.4), "liver CNP": (6,6.3), "liver CAG": (6,5.9),
 "heart p546": (5,5), "heart gfa1405": (6,6), "heart CNP": (6,6), "heart CAG": (56,56.5),
 "BA1 p546": (2,2), "BA1 gfa1405": (16,16), "BA1 CNP": (12,12), "BA1 CAG": (28,28),
 "BA2 p546": (4,3), "BA2 gfa1405": (44,45), "BA2 CNP": (21,21), "BA2 CAG": (64,63),
 "BA3 p546": (3,3), "BA3 gfa1405": (17,17), "BA3 CNP": (25,25), "BA3 CAG": (8,9),
 "liver gfa1405 dot1": (104,104), "liver gfa1405 dot2": (90,90), "liver gfa1405 dot3": (79,79), "liver gfa1405 dot4": (49,49),
 "heart CAG dot1": (72,72.3), "heart CAG dot2": (69,69.4), "heart CAG dot3": (61,61.8), "heart CAG dot4": (21,22.0),
}
def run(name, table, tol):
    n = nd = 0; worst = (0, "")
    for k, (d, h) in table.items():
        for i, (a, b) in enumerate(zip(d, h)):
            if a is None or b is None: continue
            x = dist(a, b); n += 1
            if x > worst[0]: worst = (x, f"{k} {STATS[i]} D={a} H={b}")
            if x > tol: nd += 1; print(f"  OUT OF TOLERANCE {name} {k} {STATS[i]}: D={a} H={b} dist={x:.2f}")
    print(f"{name}: {n} paired cells, {nd} beyond tol {tol}, worst {worst[0]:.2f} ({worst[1]})")
run("Fig4C percent area", pct, 0.5)
run("Fig4C RFU", rfu, 20)
n = sum(1 for _ in s1b); w = max((abs(a-b), k) for k,(a,b) in s1b.items())
print(f"Fig S1B EGFP/GAPDH x100: {n} paired cells, worst {w[0]:.1f} ({w[1]}); tolerance 3 (D) / 1.5 (H)")
print("Medians ratio p546/CAG, area: D %.3f H %.3f ; intensity: D %.3f H %.3f" % (23.2/38.7, 23.3/38.7, 128/572, 124/578))
print("Whisker-max ratio p546/CAG, area: D %.3f H %.3f ; text 41/42 = %.3f ; text intensity 154.0/474.8 = %.3f" % (41.9/42.3, 41.8/42.2, 41/42, 154.0/474.8))
print("gfa1405 liver (81) over its brain areas, by area: BA1 %.1f, BA2 %.1f, BA3 %.1f (D brain 16, 44, 17); HE brain 16, 45, 17: %.1f, %.1f, %.1f" % (81/16, 81/44, 81/17, 80.4/16, 80.4/45, 80.4/17))
