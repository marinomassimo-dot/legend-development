# build_views_k2_adv066.py: the AFTER2 view builder of the K2 round (2026-11-18), the round-1 builder with the two outcome cells of the comparison rows added; saved as it was run. BEFORE and AFTER views of this round are the round-1 views, byte-identical (round-1 builder rebuilt them: cmp equal). Scratch paths, a record of what was built, not a tool.
# build_views_adv066.py: the inline script that built views/view_INV0*_{BEFORE,AFTER}.txt on 2026-11-18 21:25 UTC, saved exactly as it was run (IT57, ADV-066).
# The paths are those of the scratch run (/tmp/it56_iso, /tmp/it56_pkg66/baseline = the generator outputs saved before the change); it is a record of what was built, not a tool.
# The pre-registration names this script as build_views.py; it was run inline and not saved under that name.
import csv
K2=True
G='/tmp/it56_iso/disease-models/wwox/research/drug_repurposing/generation_it40_20261109/'
B='/tmp/it56_pkg66/baseline/'
def rows(path): return list(csv.DictReader(open(path),delimiter='\t'))
# BEFORE view for the thread INV-04 and INV-09: what the generator in use hands a reader for these two investigations (baseline output) plus the stored investigation row text
inv={r['inv_id']:r for r in csv.DictReader(open('/tmp/it56_iso/disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations.tsv'),delimiter='\t')}
def card(i):
    r=inv[i]; return f"INVESTIGATION {i}: {r['intervention']}\nQuestion: {r['question']}\nDecisive uncertainty: {r['decisive_uncertainty']}\nNext test: {r['next_test']}\n"
fields=['starting_observation_and_chain','context','competing_explanations','premise_and_action','compound_or_probe_named_by_package','source_and_limits','expected_result_by_explanation','decision_measure','reopen_or_abandon']
def gen_view(path, invs):
    out=[]
    for x in rows(path):
        if x['inv_id'] in invs:
            out.append(f"--- generator row {x['proposal_id']} (kind {x['kind']})\n"+"\n".join(f"{f}: {x[f]}" for f in fields if x.get(f)))
    return "\n".join(out) or "(the generator output has no row for these investigations)"
for tag,pack in (('AFTER2',G+'conditional_proposals_packages_it47.tsv'),):
    txt=card('INV-04')+"\nWHAT THE CONDITIONAL-PROPOSAL GENERATOR HOLDS FOR INV-04:\n"+gen_view(pack,('INV-04',))
    if tag=='AFTER2':
        cr=[x for x in rows(G+'conditional_comparison_adv066.tsv') if x['inv_id']=='INV-04']
        txt+="\n\nCOMPARISON ROWS OF THE GENERATOR FOR INV-04:\n"+"\n".join(f"--- {x['comparison_id']}\nendpoint: {x['endpoint_or_question']}\ncandidates: {x['candidates']}\nevidence and limits: {x['documented_action_and_limits']}\nmore promising: {x['more_promising_statement']}\nmeasurements: {x['new_measurements_blocking_this_row']}" + (f"\nif favourable: {x['outcome_favourable']}\nif contrary: {x['outcome_contrary']}" if K2 else "") for x in cr)
        d=[x for x in rows(G+'conditional_decisive_adv066.tsv') if x['inv_id']=='INV-04']
        txt+="\n\nDECISIVE PROPOSITIONS OF THE PACKAGE:\n"+"\n".join(f"{x['prop_id']} [{x['status']}; {x['relation']}; {x['direction']}]: {x['statement']}" for x in d)
    open(f'view_INV04_{tag}.txt','w').write(txt)
    txt9=card('INV-09')+"\nWHAT THE CONDITIONAL-PROPOSAL GENERATOR HOLDS FOR INV-09:\n"+gen_view(pack,('INV-09',))
    if tag=='AFTER2':
        cr=[x for x in rows(G+'conditional_comparison_adv066.tsv') if x['inv_id']=='INV-09']
        txt9+="\n\nCOMPARISON ROWS OF THE GENERATOR FOR INV-09:\n"+"\n".join(f"--- {x['comparison_id']}\nendpoint: {x['endpoint_or_question']}\ncandidates: {x['candidates']}\nevidence and limits: {x['documented_action_and_limits']}\nmore promising: {x['more_promising_statement']}\nmeasurements: {x['new_measurements_blocking_this_row']}" + (f"\nif favourable: {x['outcome_favourable']}\nif contrary: {x['outcome_contrary']}" if K2 else "") for x in cr)
        d=[x for x in rows(G+'conditional_decisive_adv066.tsv') if x['inv_id']=='INV-09']
        txt9+="\n\nDECISIVE PROPOSITIONS OF THE PACKAGE:\n"+"\n".join(f"{x['prop_id']} [{x['status']}; {x['relation']}; {x['direction']}]: {x['statement']}" for x in d)
    open(f'view_INV09_{tag}.txt','w').write(txt9)
import os
for f in sorted(os.listdir('.')): print(f, len(open(f).read().split()), 'words')
