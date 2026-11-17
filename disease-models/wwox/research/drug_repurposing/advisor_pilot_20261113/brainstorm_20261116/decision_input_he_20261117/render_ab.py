import sys, re, json
sys.path.insert(0,"framework/scripts")
import strategic_advisor as sa
c=sa.ROOT/"disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113"
obs=sa.observe(c,{})
new_c, new_r = sa._compact, sa.render_assignment_states
def old_r(states):
    return json.dumps({k: {"recipient": v["recipient"], "key": v["key"], "origin": v.get("origin", "assessment"), "highest": v["highest"], "mandates": v.get("mandates", [])} for k, v in states.items()}, indent=1) or "none"
def sizes(t):
    return {p.split("\n",1)[0][:60]: len(p) for p in re.split(r"(?m)^(?=## )",t)}
sa._compact=lambda o: json.dumps(o, indent=1); sa.render_assignment_states=old_r
before=sa.build_brief_p(c,obs)
sa._compact, sa.render_assignment_states = new_c, new_r
after=sa.build_brief_p(c,obs)
open(sys.argv[1],"w").write(before); open(sys.argv[2],"w").write(after)
b,a=sizes(before),sizes(after)
print("TOTAL before",len(before),"after",len(after),"saved",len(before)-len(after), f"{(len(before)-len(after))/len(before):.1%}")
for k in b:
    if b[k]!=a.get(k): print(f"{k:62s} {b[k]:6d} -> {a.get(k)}")
# information check: every ADV id, key, recipient, highest, mandate task, verdict and path of the old render is in the new
st=sa.assignment_states(c)
miss=[]
for k,v in st.items():
    for x in (k,v["recipient"],v["key"],v["highest"]):
        if x not in after: miss.append(x)
    for m in v.get("mandates",[]):
        for x in (m["task"],m["verdict"],m["path"]):
            if x not in after: miss.append(x)
print("assignments",len(st),"items missing in the new render:",miss)
