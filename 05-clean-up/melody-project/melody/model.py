"""Bigram model utilities: token helpers and model building/printing."""
from collections import Counter, defaultdict
from typing import List, Dict, Tuple

Melody = List[str]
Bigram = Dict[str, Counter]


def add_start_end_tokens(melody: Melody) -> Melody:
    """Wrap melody with start '^' and end '$' tokens."""
    return ["^"] + melody + ["$"]


def build_bigrams(melodies: List[Melody]) -> Bigram:
    model: Bigram = defaultdict(Counter)
    for m in melodies:
        for i in range(len(m) - 1):
            curr, nxt = m[i], m[i + 1]
            model[curr][nxt] += 1
    return model


def print_bigram(model: Bigram) -> None:
    for curr, counter in model.items():
        items = dict(sorted(counter.items(), key=lambda kv: kv[1], reverse=True))
        print(f"{curr} -> {items}")


def most_common_transition(model: Bigram) -> Tuple[str, str, int]:
    best = ("", "", -1)
    for curr, counter in model.items():
        if not counter:
            continue
        nxt, cnt = counter.most_common(1)[0]
        if cnt > best[2]:
            best = (curr, nxt, cnt)
    return best
