"""IT40 helper: curated-passage translations after text changed.
  i18n_refresh.py tasks   -> writes consume_it40_20261109/translate_tasks.json (one task per curated passage missing in a language file or stale)
                             mode EDIT when an older passage of HEAD is a prefix of the new one (translate only the added block, compose with the old translation),
                             mode NEW otherwise (translate the whole passage).
  i18n_refresh.py merge FILE -> merges {key: {it, fr, es, de}} (key = new passage key) into content_{it,fr,es,de}.json (composing for EDIT tasks)."""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
I18N = HERE.parent / "view/i18n"
LANGS = ("it", "fr", "es", "de")
src = json.load(open(I18N / "content_source.json"))
cur = {l: json.load(open(I18N / f"content_{l}.json")) for l in LANGS}
def head_source():
    out = subprocess.run(["git", "show", "edfa347f:disease-models/wwox/research/drug_repurposing/view/i18n/content_source.json"], capture_output=True, text=True, cwd=HERE.parents[4], check=True).stdout
    return json.loads(out)
def base_trans(l):
    out = subprocess.run(["git", "show", f"edfa347f:disease-models/wwox/research/drug_repurposing/view/i18n/content_{l}.json"], capture_output=True, text=True, cwd=HERE.parents[4], check=True).stdout
    return json.loads(out)
BASE = {l: base_trans(l) for l in LANGS}
def tasks():
    old = head_source(); T = {}
    for k, v in src.items():
        if v.get("src") != "en": continue
        need = [l for l in LANGS if k not in cur[l] or (cur[l][k] or "").startswith("⁠")]
        if not need: continue
        new = v["text"]
        best = None
        for ok, ov in old.items():
            if ov.get("src") == "en" and ov["text"] != new and new.startswith(ov["text"].rstrip()[:max(40, len(ov["text"].rstrip()) - 1)]) and ok in BASE["fr"]:
                if best is None or len(ov["text"]) > len(old[best]["text"]): best = ok
        if best and not new.startswith(old[best]["text"].rstrip()): best = None
        if best:
            T[k] = {"mode": "EDIT", "old_key": best, "old_english": old[best]["text"], "added_english": new[len(old[best]["text"].rstrip()):].strip(), "new_english": new, "langs": need}
        else:
            T[k] = {"mode": "NEW", "english": new, "langs": need}
    json.dump(T, open(HERE / "translate_tasks.json", "w"), indent=1, ensure_ascii=False)
    print(len(T), "tasks;", sum(t["mode"] == "EDIT" for t in T.values()), "EDIT")
def merge(fp):
    tr = json.load(open(fp)); T = json.load(open(HERE / "translate_tasks.json")); n = 0
    for k, t in T.items():
        for l in LANGS:
            if l not in t["langs"] or k not in tr or l not in tr[k]: continue
            text = tr[k][l]
            if t["mode"] == "EDIT":
                text = (cur[l].get(t["old_key"]) or BASE[l][t["old_key"]]).rstrip() + " " + text
            cur[l][k] = text; n += 1
    for l in LANGS:
        json.dump(cur[l], open(I18N / f"content_{l}.json", "w"), indent=1, ensure_ascii=False, sort_keys=True)
    print("merged", n)
if __name__ == "__main__":
    {"tasks": tasks, "merge": lambda: merge(sys.argv[2])}[sys.argv[1]]()
