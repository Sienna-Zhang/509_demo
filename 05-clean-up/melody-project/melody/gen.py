"""Melody generation helpers (sampling and constraints)."""
from collections import Counter
from typing import List
import random

Melody = List[str]


def weighted_choice(counter: Counter) -> str:
    keys = list(counter.keys())
    weights = [counter[k] for k in keys]
    return random.choices(keys, weights=weights, k=1)[0]


def violates_three_repeat(seq: Melody) -> bool:
    return len(seq) >= 3 and seq[-1] == seq[-2] == seq[-3]


def generate_melody(model, max_len: int = 32, forbid_three_repeats: bool = False) -> Melody:
    curr = "^"
    out: Melody = []
    for _ in range(max_len):
        if curr not in model or not model[curr]:
            break
        nxt = weighted_choice(model[curr])
        if nxt == "$":
            break

        out.append(nxt)

        if forbid_three_repeats and violates_three_repeat(out):
            alt = weighted_choice(model[curr])
            if alt != nxt:
                out[-1] = alt

        curr = out[-1]
    return out
