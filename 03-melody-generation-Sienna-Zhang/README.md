[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PRYUHfuh)
# TECHIN 509: Melody Generator with Functions & Bigrams

A naive method to generate melody is to randomly generate notes one at a time. That works, but generated melodies may sound random. Real music depends on **note-to-note relationships**. For example, if you play `C`, the next note is more likely to be `D` or `E` than `B`.

A **bigram model** stores this information:

```
Current note → possible next notes and their counts
```

Example (from a small dataset):

```
C → {D: 3, E: 1}
D → {E: 2, G: 1}
```

**Note**: The example uses music notes, which may not necessarily be the case for existing datasets. The examples are only for demo purpose.

## Instructions

### Part 1 — Write functions for clarity

Before you write code, sketch what your program will do. Your answers to Project 01 and 02 may help.

You can decide how to break the program up.

### Part 2 — Build the bigram model

Your program should be able to:
- Read a melody (lists of notes, ABC, MIDI, etc.). For reference, we will provide you a dataset of melodies represented by music notes. If you are interested in other representations, feel free to explore them.
- Build a bigram table showing “current note → next-note counts.”
- Generate new melodies using that model.
Your code must:
   - avoid long monolithic scripts,
   - be modularized and use functions meaningfully,
   - be easy for someone else to follow.
 
Below you will see two examples of melodies; both will be provided to you later as a dataset so that you can start generating melodies.

- **Example 1**: A sequence of notes without duration information: `E4 F#4 G4 A4 B4 A4 G4 F#4 E4`, where `#` represents one semitone up, `C4` denotes C in the 4th octave, `C5` denotes the C one octave higher than C4. Similar logic applies to other pitches.
- **Example 2**: A sequence of notes with duration information: `F4_1.3 A4_0.45 F4_0.45 A4_0.45 A#4_1.34 D5_0.45 A#4_0.45 D5_0.45 F5_2.23`, where `_x` represents `x` number of beats. You can convert beats to time by $time = 60*beats/tempo$, and feel free to define your own tempo.


### Part 3 — Generate new melodies

* Start with a random note. While your melody isn’t long enough:
  * Look up for the next notes based on the current note.
  * Choose one at random, weighted by counts.
  * Append it to your melody.
* Print the melody as output.

### Part 4 — Show your results

* Print your bigram model in a readable way.
* Generate and print at least **3 sample melodies**.

Example output:

```
Bigram model:
C → {'D': 3, 'E': 1}
D → {'E': 2, 'G': 1}
...

Generated melodies:
1. C D E G C D
2. G F E D C E
3. E F G A C D
```

### Part 5 — Clean Up

* If we follow the bigram model, melody generation never stops. To prevent this situation,  add **start (`^`)** and **end (`$`)** tokens so melodies can stop naturally.
* Write a function to find the **most common transition** in the dataset.
* **Optional**: Add constraints: e.g., forbid repeating the same note 3+ times in a row. Feel free to define your own set of constraints.
* Test your new code and generate longer melodies and see if they sound “more musical” than unigram ones.

