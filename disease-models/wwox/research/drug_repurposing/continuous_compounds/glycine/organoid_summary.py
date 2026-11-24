"""Summarize verified GRIN1 counts under the frozen per-library coverage rule."""
import csv
from hashlib import sha256
from pathlib import Path
from statistics import mean
import sys

def records(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))

def summarize(folder, stream):
    manifest = records(folder/"runs.tsv")
    assert len({r["run_accession"] for r in manifest}) == len(manifest) == 6
    probe_hash = sha256((folder/"junction_probes.tsv").read_bytes()).hexdigest()
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("run","group","rule","Q","included","skipped","conflict","informative","fraction","status"))
    fractions = {"control":[], "KO":[]}
    conditions = {("centered","20"),("centered","30"),("any","20"),("any","30")}
    for run in sorted(manifest, key=lambda x:x["run_accession"]):
        name = run["run_accession"]
        group = "control" if "untreated" in run["sample_title"] else "KO"
        assert group == "control" or "KO/WWOX" in run["sample_title"]
        path = folder/"organoid_counts"/(name+".tsv")
        if not path.exists():
            writer.writerow((name,group,"","","","","","","","pending"))
            continue
        rows = records(path)
        assert len(rows)==4 and {(r["rule"],r["Q"]) for r in rows}==conditions
        for r in rows:
            assert (r["run"],r["sample"],r["bytes"],r["compressed_md5"],r["reads"],r["probe_sha256"]) == (
                name,run["sample_title"],run["fastq_bytes"],run["fastq_md5"],run["read_count"],probe_hash)
            inc, skip, conflict = (int(r[k]) for k in ("included","skipped","conflict"))
            assert min(inc,skip,conflict)>=0 and inc+skip+conflict<=int(r["reads"])
            total = inc+skip
            primary = (r["rule"],r["Q"])==("centered","20")
            status = ("eligible" if total>=20 else "low_coverage") if primary else "sensitivity"
            if primary and total>=20:
                fractions[group].append(inc/total)
            writer.writerow((name,group,r["rule"],r["Q"],inc,skip,conflict,total,
                             f"{inc/total:.4f}" if total else "NA",status))
    if len(fractions["control"])==2 and len(fractions["KO"])==4:
        effect=100*(mean(fractions["KO"])-mean(fractions["control"]))
        return f"Six libraries eligible. Equal-library KO minus control: {effect:.2f} percentage points."
    return "Genotype contrast withheld under the frozen six-library coverage rule."

if __name__=="__main__":
    print(summarize(Path(sys.argv[1]),sys.stdout),file=sys.stderr)
