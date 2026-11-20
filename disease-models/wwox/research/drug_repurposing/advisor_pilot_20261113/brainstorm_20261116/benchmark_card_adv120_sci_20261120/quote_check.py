"""ADV-120 sitting 2: verify that every sentence quoted in the card occurs verbatim (whitespace and hyphen variants
normalised) in the held full text. Usage: quote_check.py <obeid.xml> <repudi2021.xml> <mmc2.txt>   (mmc2.txt = pdftotext of mmc2.pdf)"""
import html, re, sys

def norm(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = s.replace('‐', '-').replace('‑', '-').replace('–', '-').replace('’', "'")
    return re.sub(r'\s+', '', s)

def load(p):
    return norm(open(p, encoding='utf-8', errors='replace').read())

obeid, repudi, mmc2 = (load(p) for p in sys.argv[1:4])
Q = [
 ('O', "LD treatment modestly, though significantly, extended lifespan relative to untreated Wwox-null controls"),
 ('O', "HD produced survival comparable to WT animals (p = 0.78), and significantly extended survival relative to the LD group (p < 0.0001) and the KO + RI controls (p < 0.0001)"),
 ('O', "LD also significantly improved survival compared with the KO + RI controls (p < 0.0001)"),
 ('O', "Statistical analysis was performed using Student's t test"),
 ('O', "Error bars represent mean ± SD"),
 ('O', "LD-treated mice did not survive to P90"),
 ('O', "By P20, glucose levels in HD-treated mice were fully normalized and comparable to WT controls, whereas LD-treated mice showed an intermediate improvement"),
 ('O', "From P30 onward, glucose levels were normalized across all groups"),
 ('O', "LD treatment resulted in partial improvement and HD treatment achieved near-complete rescue"),
 ('O', "with no significant sex-dependent differences observed"),
 ('O', "Percentages (E) indicate relative MBP intensity compared with WT"),
 ('O', "demonstrating dose-dependent restoration of myelination across CC, striatum, and cortex"),
 ('O', "Although based on a limited cohort"),
 ('O', "We also cannot exclude that the optimal dose was not achieved"),
 ('O', "WWOX expression levels were not normalized across promoter conditions"),
 ('O', "Therapeutic intervention beyond this period was not feasible"),
 ('O', "Treated mice exhibited a dramatic extension in survival, from approximately three weeks to nearly one year"),
 ('O', "(C) A graph representing body weight during the first postnatal month in KO + LD and KO + HD mice, with weights reaching near WT levels by postnatal day 30"),
 ('O', "Long-term growth monitoring demonstrated sustained weight gain and normalization in KO + HD mice up to 180 days of age"),
 ('O', "(E-G) Blood glucose levels (mg/dL) measured at postnatal days 10, 20, and 30"),
 ('O', "key gaps regarding optimal dosing and safety remained"),
 ('O', "Although no overt toxicity was observed in prior studies"),
 ('O', "absence of off-target hepatic expression"),
 ('R', "we observed some minor differences in the g-ratio and the number of unmyelinated axons"),
 ('R', "Graph represents the number of unmyelinated axons (corpus callosum) per FOV"),
 ('R', "WT (n = 3), KO (n = 3), or KO mice injected with AAV9-hSynI-mWwox (n = 3) per field of view (FOV)"),
 ('R', "Error bars represent ± SD. (** P < 0.01, *** P < 0.001, Student's t-test)"),
 ('M', "Differential quantification of microglia (F) and astrocytes (H) in each treatment"),
 ('M', "Error bars represent mean ± SD"),
 ('M', "Statistical analysis was performed using Student's t-test (***p<0.001, ****p < 0.0001, ns: not significant)"),
 ('M', "Kaplan-Meier survival analysis (till P40) of Wwox-null treated with AAV9-hSyn1-hWWOX (2.63x1011 vg) at P1-P5 (n=3-7)"),
 ('M', "A graph representing quantification of hindlimb clasping in wild-type (WT), Wwox-null (KO), and AAV9-Syn1-WWOX-treated KO mice receiving LD"),
]
src = {'O': obeid, 'R': repudi, 'M': mmc2}
bad = 0
for k, q in Q:
    ok = norm(q) in src[k]
    bad += (not ok)
    print(('FOUND   ' if ok else 'MISSING ') + k + ' ' + q[:110])
print('quotes %d, found %d, missing %d' % (len(Q), len(Q) - bad, bad))
