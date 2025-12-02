"""I/O utilities for reading and writing melody datasets."""
from typing import List
import os

Melody = List[str]


def parse_melody(line: str) -> Melody:
    """Split a space-separated melody line into tokens.

    Keeps duration tokens (e.g., `F4_1.3`) as single tokens.
    """
    return [tok for tok in line.strip().split() if tok]


def load_melodies(path: str) -> List[Melody]:
    """Load melodies from `path`.

    - If `path` is a directory, each file is read and its whole content is
      parsed as a single melody (suitable for the provided dataset files).
    - If `path` is a file, it is treated as text file with one melody per line.

    Returns an empty list and prints a helpful message on FileNotFoundError.
    """
    melodies: List[Melody] = []

    try:
        if os.path.isdir(path):
            for fname in sorted(os.listdir(path)):
                fpath = os.path.join(path, fname)
                if not os.path.isfile(fpath):
                    continue
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        text = f.read().strip()
                        if not text:
                            continue
                        melodies.append(parse_melody(text))
                except Exception:
                    # skip unreadable files
                    continue
        else:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    melodies.append(parse_melody(line))

    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Please make sure the dataset file exists.")

    return melodies


def save_melodies(melodies: List[Melody], path: str) -> None:
    """Save generated melodies to a file, one melody per line."""
    with open(path, "w", encoding="utf-8") as f:
        for melody in melodies:
            line = " ".join(melody)
            f.write(line + "\n")
