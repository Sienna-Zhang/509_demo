"""Melody project main module.

Provides utilities to load/save melodies, build a bigram model,
generate melodies, and a simple CLI entry point.
"""
import argparse
import os
import sys
import random

from melody.io import load_melodies, save_melodies
from melody.model import add_start_end_tokens, build_bigrams, print_bigram, most_common_transition
from melody.gen import generate_melody


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate melodies from bigram model.")
    # default dataset lives inside this folder under `dataset/note_seq_w_dur`
    default_data = os.path.join(os.path.dirname(__file__), "dataset", "note_seq_w_dur")
    parser.add_argument("--data", type=str, default=default_data,
                        help="Path to dataset file or directory (default: ./dataset/note_seq_w_dur)")
    parser.add_argument("--out", type=str, default=None, help="Optional output file to save generated melodies")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--samples", type=int, default=3, help="How many melodies to generate")
    parser.add_argument("--max-len", type=int, default=32, help="Max tokens per generated melody")
    parser.add_argument("--forbid-three", action="store_true", help="Forbid 3 identical notes in a row")

    args = parser.parse_args(argv)

    random.seed(args.seed)

    melodies_raw = load_melodies(args.data)
    if not melodies_raw:
        print("No melodies loaded. Exiting.")
        return 1

    melodies = [add_start_end_tokens(m) for m in melodies_raw]
    model = build_bigrams(melodies)

    print("Bigram model (sample):")
    print_bigram(model)
    print()

    generated = []
    print("Generated melodies:")
    for i in range(1, args.samples + 1):
        m = generate_melody(model, max_len=args.max_len, forbid_three_repeats=args.forbid_three)
        clean = [x for x in m if x not in {"^", "$"}]
        print(f"{i}.", " ".join(clean))
        generated.append(clean)

    print()
    c, n, k = most_common_transition(model)
    print(f"Most common transition: {c} -> {n} ({k})")

    if args.out:
        save_melodies(generated, args.out)
        print(f"Saved {len(generated)} melodies to {args.out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
