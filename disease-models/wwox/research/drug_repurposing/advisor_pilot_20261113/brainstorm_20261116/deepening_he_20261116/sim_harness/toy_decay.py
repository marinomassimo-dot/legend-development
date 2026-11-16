"""Toy adapter for the bisect tests: rel falls as exp(-k x), with a tiny seeded jitter; rise as exp(+k x). No claim about any system."""
import math
PARAMS = {"x": [0.0, 0.0, 3.0, "strength"], "k": [1.0, 0.0, 5.0, "rate"], "sign": [-1.0, -1.0, 1.0, "-1 falls, +1 rises"]}
def simulate(params, seed):
    j = 1.0 + 0.001 * ((int(seed) % 3) - 1)
    return {"rel": math.exp(params["sign"] * params["k"] * params["x"]) * j}
