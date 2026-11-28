"""Screen untreated WWOX expression for arginine recycling and competing sinks."""
from pathlib import Path
import sys
repo, files, output = map(Path, sys.argv[1:])
sys.path.insert(0, str(repo / "disease-models/wwox/research/drug_repurposing/continuous_compounds/thiamine"))
from screen import run
run(files, target_genes=["Ass1", "Asl", "Nos1", "Nos2", "Nos3", "Arg1", "Arg2", "Ddah1"],
    output=output, missing_value="NA")
