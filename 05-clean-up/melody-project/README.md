# Melody Project

This project converts the student notebooks into a small, structured Python
package and a command-line entry point for building a simple bigram melody
model and generating new melodies.

## Project layout (files & responsibilities)

- `main.py`
  - CLI entry point. Loads the dataset, builds the bigram model, prints a
    sample of the model, generates sample melodies, and optionally saves
    generated melodies to a file. Keeps orchestration logic minimal.

- `test.py`
  - Unit tests using Python's `unittest`. Tests cover `load_melodies`,
    `save_melodies`, handling of missing files, and a small bigram check.

- `melody/` (package)
  - `__init__.py`: Public exports for convenience.
  - `io.py`: All I/O responsibilities—`parse_melody`, `load_melodies`, and
    `save_melodies`. Keeps file-format handling isolated so other modules are
    pure logic.
  - `model.py`: Bigram model helpers—`add_start_end_tokens`, `build_bigrams`,
    `print_bigram`, and `most_common_transition`. Pure data-processing code.
  - `gen.py`: Melody generation and sampling—`weighted_choice`,
    `generate_melody`, and simple generation constraints (e.g., forbid 3
    repeats). Kept separate so generation logic can evolve independently.

- `dataset/`
  - `note_seq_w_dur/` and `note_seq_wo_dur/` (subfolders). The project now
    includes the dataset locally under this folder. By default `main.py`
    points to `dataset/note_seq_w_dur`.

- `README.md` (this file)
  - Usage notes, quick examples, and the project structure summary.

**Design summary**: each module has a narrow responsibility: I/O, model
construction, or generation. `main.py` orchestrates these modules only.

## Usage

- Run the main script to build a model and generate melodies (PowerShell):

  ```powershell
  python main.py --data "dataset\note_seq_w_dur" --samples 5 --max-len 40
  ```

- Save generated melodies to a file:

  ```powershell
  python main.py --data "dataset\note_seq_w_dur" --samples 10 --out generated.txt
  ```


- Run the unit tests with:

  ```powershell
  python -m unittest test.py
  ```
