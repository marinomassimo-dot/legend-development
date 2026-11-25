import json, runpy, os, re
J=os.environ["CLAUDE_JOB_DIR"]+"/tmp/inc2/"
d=runpy.run_path(J+"edits_it23b.py")
R="disease-models/wwox/research/drug_repurposing/cards/"
A="disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv282_null_note_control_audit_sci_20261125/"
m={"DA-GSE-PDK-003":("E03_pdk_inhibition_dca",["T01","T02","T03"]),"DA-I01-001":("I01_pdk_inhibition_dca_premise_seizure_glycaemia",["T04","T05","T06"]),
"DA-L01-003":("L01_nrf2_axis",["T07","T08","T09"]),"DA-L01-001":("L01_nrf2_axis",["T10","T11","T12"]),"DA-W2-012":("F02_myelination_activity_sign",["T13"]),
"DA-J01-007":("J01_glial_reactivity_modulation",["T14","T15","T16"]),"DA-J01-006":("J01_glial_reactivity_modulation",["T17"]),"DA-J01-002":("J01_glial_reactivity_modulation",["T18","T19"]),
"DA-K01-002":("K01_hif_axis_glycolytic_shift",["T20","T21","T22","T23"]),"DA-K01-008":("K01_hif_axis_glycolytic_shift",["T24","T25"]),
"DA-M01-002":("M01_neurogenic_output_myc_window",["T26","T27"]),"DA-M01-007":("M01_neurogenic_output_myc_window",["T28"]),"DA-W2-002":("F01_glutamate_receptor_node",["T29","T30","T31"])}
ed={x["id"]:x for x in d["EDITS"]}
t2=open(A+"BLIND_SENTENCES_ADV282_INC2_SCI_20261125.md").read(); blocks={}
for b in re.split(r"\n(?=## DA-)",t2)[1:]:
    i=b.split("\n")[0][3:].strip(); blocks[i]=b[b.index("Held source files"):].strip()
h1=open(A+"BLIND_SENTENCES_ADV282_INC1_SCI_20261125.md").read(); h1=h1[h1.index("Held source files for every block"):h1.index("## DA-")].strip()
out=["# Sentences for the blind check, IT23 increment 2 (2026-11-25)\n\nEach block below is a card note as it would stand after a proposed edit. Judge the WHOLE note against the held sources, clause by clause. Hypothesis-level reading of public data; not medical advice.\n"]
for i,(card,ids) in m.items():
    p=json.load(open(R+card+".packet.json")); a=[x for x in p["disease_assertions"] if x["id"]==i][0]
    f="measured_result_note" if "measured_result_note" in a else "note"; s=a[f]; before=s
    for k in ids:
        x=ed[k]; assert x["old"] in s,(k)
        s=s.replace(x["old"],x["new"]) if x["mode"]=="replace" else s.replace(x["old"],x["old"]+x["new"])
    if s.count("(")!=s.count(")"): print("PAREN",i,s.count("("),s.count(")"),"before",before.count("("),before.count(")"))
    src=blocks.get(i) or h1+("\n(GSE150123 is for a culture-time statement only.)" if i in("DA-K01-002","DA-J01-007") else "")
    out.append(f"\n## {i}\n\nRow fields: target_id: {a['target_id']}; endpoint: {a['endpoint']}\n\nNote as proposed (whole):\n\n> {s}\n\nSource label the repository gives: {a['source']}\n\n{src}\n")
out.append("\n---\nRules of the check: open only the held sources named in each block. Do not open any other file of the repository (no RESULT, BLIND_REPORT, card, ledger, dossier, packet, checkpoint or git history). Recompute every number you can; mark values read from a figure image 'by eye'; for an absence claim name the search terms; say 'NOT CHECKED' for what no held source can settle.\n")
open(J+"SENTENCES_C.md","w").write("".join(out)); print(len("".join(out)))
