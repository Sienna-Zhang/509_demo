# Problem-Solving using Python
## Input
**What information does the program need to start?**

It needs some basic input parameters to determine the foundation of the music. The most essential parameters include the time signature, scale, and total music length.

**Shall the program request input from users? Make a case for your answer rather than simply give yes or no.**

Yes. At the very least, the user needs to give the program a command to start generating music. In addition, users can adjust personalized parameters to produce music in different styles.
## Output
**What does the program produce?**

I think it should produce a set of data that includes at least the note (represented by a number) and the duration of that note.

**What the generated music might look like, e.g., figures, excel spreadsheet, plain text?**

I think a spreadsheet format would be better, since it needs to record at least two columns of data: notes and time.
## Representation
**How should the program represent notes? Some examples might include letters (C, D, E), numbers (music signal frequencies), strings (C4 quarter note).**

The most basic way is to use the numbers 1–7 (Do Re Mi Fa So La Si) to represent a natural scale. A letter prefix can be added to indicate different octaves (for example, A1, A2, A3, A4, A5, A6, A7).

**How to capture/represent time duration of music notes?**

First, the duration of one beat in seconds should be defined according to the tempo, and then the note’s duration can be represented by the number of beats it lasts.
## Logic
**How could the program decide what note comes next?**

The program can be given melodic curves derived from classic examples of different music styles. Once the initial pitch is set, the curve can be used to determine the following notes. By introducing random variations at certain points on the curve, the program can ensure that about 80% of the generated music follows the intended melody while 20% allows for variation, which keeps the music interesting and pleasant.

**How does the program know when to terminate music generation?**

The desired music length can be set as one of the initial input parameters. To ensure completeness, this time unit can be defined in measures (bars).
## Extensions
**What are blockers for generating longer piece of music?**

1. When the range of variation (randomness) is insufficient, the longer the generated music becomes, the more repetitive it will sound.
2. The program lacks a memory mechanism and therefore cannot reference previously generated content. As the music becomes longer, this can lead to overall melodic repetition (in the random portions) or overly abrupt transitions.