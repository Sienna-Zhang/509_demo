"""Simple melody package exposing IO, model, and generation helpers."""
from .io import parse_melody, load_melodies, save_melodies
from .model import add_start_end_tokens, build_bigrams, print_bigram, most_common_transition
from .gen import generate_melody

__all__ = [
    "parse_melody",
    "load_melodies",
    "save_melodies",
    "add_start_end_tokens",
    "build_bigrams",
    "print_bigram",
    "most_common_transition",
    "generate_melody",
]
