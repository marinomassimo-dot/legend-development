"""Scratch driver around BioPathNet b051a900 (not committed with third-party code).
usage: drive.py SRC DATA CKPT OUT mode   mode in {sanity, predict, visualize}
"""
import sys, os, json, time, resource
SRC, DATA, CKPT, OUT, MODE = sys.argv[1:6]
sys.path.insert(0, SRC)
import torch
from easydict import EasyDict
from torchdrug import core, data as tdata
from biopathnet import dataset, layer, model, task, util  # noqa: F401 (registers classes)

torch.manual_seed(1024)
torch.set_num_threads(2)
files = {"sanity": "test_sample100.txt", "predict": "test_pred.txt", "visualize": "test_vis.txt"}[MODE]
cfg = EasyDict({
    "dataset": {"class": "biomedical", "path": DATA, "include_factgraph": True,
                "files": ["train1.txt", "train2.txt", "valid.txt", files]},
    "task": {"class": "KnowledgeGraphCompletionBiomed",
             "model": {"class": "NBFNet", "input_dim": 32, "hidden_dims": [32] * 6, "message_func": "distmult",
                       "aggregate_func": "pna", "short_cut": True, "layer_norm": True, "dependent": True,
                       "remove_one_hop": True},
             "criterion": "bce", "num_negative": 32, "strict_negative": True, "adversarial_temperature": 1,
             "sample_weight": False, "heterogeneous_negative": True, "heterogeneous_evaluation": True,
             "full_batch_eval": True, "remove_pos": MODE == "sanity"},
    "optimizer": {"class": "Adam", "lr": 5.0e-3},
    "engine": {"gpus": None, "batch_size": 2},
    "checkpoint": CKPT,
})
t0 = time.time()
ds = core.Configurable.load_config_dict(cfg.dataset)
solver = util.build_solver(cfg, ds)
model_ = solver.model
model_.eval()
t_load = time.time() - t0
ent = ds.entity_vocab
rel = ds.relation_vocab
nrel = len(rel)
test = solver.test_set
res = {"mode": MODE, "load_s": round(t_load, 1), "n_queries": len(test), "relations": list(rel)}

if MODE in ("sanity", "predict"):
    loader = tdata.DataLoader(test, 2)
    rows, rr_t, rr_h = [], [], []
    t1 = time.time()
    with torch.no_grad():
        for batch in loader:
            pred, (mask, target) = model_.predict_and_target(batch)
            pos = pred.gather(-1, target.unsqueeze(-1))
            rank = (torch.sum((pos <= pred) & mask, dim=-1) + 1).float()
            for i in range(len(batch)):
                h, t, r = batch[i].tolist()
                rr_t.append(1.0 / rank[i, 0].item()); rr_h.append(1.0 / rank[i, 1].item())
                if MODE == "predict":
                    m = mask[i, 0]
                    sc = pred[i, 0][m]
                    idx = m.nonzero().squeeze(-1)
                    order = torch.argsort(sc, descending=True)
                    rows.append({"query": ent[h], "relation": rel[r],
                                 "ranked": [[ent[idx[j]], round(float(sc[j]), 4)] for j in order.tolist()]})
    res["infer_s"] = round(time.time() - t1, 1)
    if MODE == "sanity":
        res["mrr_tail"] = sum(rr_t) / len(rr_t); res["mrr_head"] = sum(rr_h) / len(rr_h)
        res["mrr_both"] = (sum(rr_t) + sum(rr_h)) / (2 * len(rr_t))
        res["hits10_tail"] = sum(1 for x in rr_t if x >= 0.1) / len(rr_t)
    else:
        res["predictions"] = rows
else:
    out = []
    t1 = time.time()
    for i in range(len(test)):
        trip = test[i]
        h, t, r = trip.tolist()
        sample = torch.as_tensor([[h, t, r]])
        pred, (mask, target) = model_.predict_and_target(sample)
        pos = pred.gather(-1, target.unsqueeze(-1))
        rank = int((torch.sum((pos <= pred) & mask, dim=-1) + 1)[0, 0])
        paths, weights = model_.visualize(sample)
        ps = []
        for path, w in zip(paths, weights):
            steps = []
            for a, b, rr in path:
                inv = rr >= nrel
                steps.append({"h": ent[a], "r": rel[rr % nrel] + ("^(-1)" if inv else ""), "t": ent[b]})
            ps.append({"weight": float(w), "steps": steps})
        out.append({"query": [ent[h], rel[r], ent[t]], "rank_tail": rank, "paths": ps})
    res["infer_s"] = round(time.time() - t1, 1)
    res["explanations"] = out
res["maxrss_gb"] = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2)
json.dump(res, open(os.path.join(OUT, f"{MODE}.json"), "w"), indent=1)
print({k: v for k, v in res.items() if k not in ("predictions", "explanations", "relations")})
