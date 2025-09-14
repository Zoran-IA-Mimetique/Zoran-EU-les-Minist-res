#!/usr/bin/env python3
# POC_FairDispatch_Sante.py — allocation équitable (UCB1 simple)

import math, random

random.seed(42)
centers = [
  {"name": "Centre_A", "n": 1, "reward": 0.75},
  {"name": "Centre_B", "n": 1, "reward": 0.70},
  {"name": "Centre_C", "n": 1, "reward": 0.65},
]

def ucb1_value(c, t):
    return c["reward"] + math.sqrt(2*math.log(t)/c["n"])

def dispatch(patients=100):
    logs = []
    for t in range(1, patients+1):
        idx = max(range(len(centers)), key=lambda i: ucb1_value(centers[i], t+1))
        chosen = centers[idx]
        outcome = 1 if random.random() < chosen["reward"] else 0
        chosen["n"] += 1
        chosen["reward"] = (chosen["reward"]*(chosen["n"]-1) + outcome)/chosen["n"]
        logs.append((t, chosen["name"], outcome, chosen["reward"]))
    return logs

if __name__ == "__main__":
    logs = dispatch(200)
    allocation = {}
    for _, name, _, _ in logs:
        allocation[name] = allocation.get(name, 0) + 1
    total = sum(allocation.values())
    fairness = 1 - (max(allocation.values()) - min(allocation.values()))/total
    print("Allocations:", allocation)
    print("Fairness_index_simplified:", round(fairness, 3))
