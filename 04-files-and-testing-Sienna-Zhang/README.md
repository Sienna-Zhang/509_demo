[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/H4HEQ37g)
# TECHIN 509: Melody Generator with Files & Testing

In this assignment, you will:
* Save and load melodies from files so your work is reproducible.
* Write simple tests to check that your functions behave correctly.
* Strengthen habits of writing **reliable, reusable code**.


## Instructions

### Part 1 — Work with Files

1. **Load dataset from a file**

   * Create a folder `data/` and store the melody dataset there.
   * Write a function:

     ```python
     def load_melodies(path: str) -> list[list[str]]:
         """Read melodies from a file and return as list of note lists."""
     ```
    Two sample datasets created based on [NES melodies](https://github.com/chrisdonahue/nesmdb) is provided: one dataset contains duration information for music notes, whereas another does not contain duration information.
    **Note**: Feel free to use other datasets to generate melodies. 

3. **Save generated melodies to a file**

   * Write a function:

     ```python
     def save_melodies(melodies: list[list[str]], path: str) -> None:
         """Save a list of generated melodies to a file, one melody per line."""
     ```

4. **Robustness**

   * Use `try/except` when reading files: if the file is missing, print a helpful message instead of crashing.
   * Example:

     ```
     File not found: data/melodies.txt
     Please make sure the dataset file exists.
     ```

---

### Part 2 — Add Testing

1. **Use Python’s built-in `unittest`**
   * Create a folder `tests/` with a file `test_models.py`.
2. **Write at least 3 tests**. 
3. **Run your tests**
