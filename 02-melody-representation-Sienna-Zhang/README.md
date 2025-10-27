[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hVyU_Tf_)

# TECHIN 509: Melody Representation

This assignment aims to get you proceed with project. This assignment is about thinking with Python structure, rather than writing fancy code.

## Instructions
### Q1:
- Based on our in-class discussion, **how can you store a sequence of notes like C D E F G in Python**? Please be specific and give the actual code to represent the example note sequence. Justify your answer carefully!

    Below are some questions to help you starting addressing the problem above:
    1. If a melody is like a sentence, what would each word be?
    2. Which Python type keeps items in order (so you know which note comes first, second, third)? Note that this positional information is critical to music.
    3. How to group several melodies together?
### Answer:
If a melody is like a sentence, then each note is like a word — it’s one unit in the musical sequence.
Because the order of notes is essential (we must know which note comes first, second, third, etc.), we should use a Python list, which preserves order and allows repeated elements.

Here’s the Python code to represent the melody C D E F G:
```py
melody = ["C", "D", "E", "F", "G"]
```

Each element in the list is one musical note, and the order in the list represents the time order in which notes are played.

If we want to store several melodies together, we can use another list (a list of lists) or a dictionary to group them by name, for example:
```py
melodies = {
    "theme_1": ["C", "D", "E", "F", "G"],
    "theme_2": ["G", "F", "E", "D", "C"]
}
```
### Q2:
- Based on your choice of note representation, if you are given a set of melodies to "teach/train" your music composer, how do you prefer the data being stored?

    Below are some questions to help you starting addressing the problem above:
    1. If I have a collection of my chosen data type, how can I “flatten” them into one?
    2. Can I start with an empty list `all_notes = []` and then add the notes from each melody?
    3. What tool do I know that combines lists?
### Answer:
If I represent each melody as a list of notes, then a collection of melodies can naturally be stored as a list of lists — each inner list is one melody.

When training a model (or a “music composer”), I may want to have all the notes in a single long sequence rather than separated melodies.
In that case, I can flatten the data by starting with an empty list and adding all notes from each melody:
```py
melodies = [
    ["C", "D", "E", "F", "G"],
    ["G", "F", "E", "D", "C"],
    ["A", "B", "C", "A"]
]

# Start with an empty list
all_notes = []

# Add notes from each melody
for melody in melodies:
    all_notes.extend(melody) 

print(all_notes)
```
### Q3:
- Suppose you are given a set of melodies, what information would you like to extract to "teach/train" your music composer?
### Answer:
If I am given a set of melodies, I would extract three key types of information to train my music composer:

Duration : how long each note lasts.

Rhythm : the timing and spacing between notes.

Dynamics : how strong or soft each note is played.

These features help the model learn not only which notes to play, but also how to play them, giving the generated music a more natural and expressive quality.



**Note**: We do not grade this submission based on correctness. In fact, there may not exist a correct answer, rather these answers are your design choices. But you **should justify your answers/choices.**