Write a program that is the reverse of the previous one: now the user thinks of
a number and the computer tries to guess it. To the attempts of the computer the
user must answer with a letter: "L" for lower if the number to guess is lower,
"H" for higher if the number to guess is higher, and "C" for correct (you can
use the `input()` function for that). When the computer has guessed the number,
it prints how many attempts were needed. Make sure the computer also recognises
that no answer is possible any more (maybe because the user made a mistake, or
because the user was trying to fool the computer). A smart program has to guess
at most ten times.

### Assignment

The user thinks of a number between 1 and 1000 (limits included). Ten attempts
only suffice if the computer halves the range of numbers that are still possible
with every guess. The computer therefore keeps track of the smallest and the
largest number that is still possible, and always guesses the middle of that
range, rounded down. The first guess is thus $$(1 + 1000) // 2 = 500$$.

If the user answers `L`, the largest possible number becomes the guess minus
one. If the user answers `H`, the smallest possible number becomes the guess
plus one. As soon as the smallest possible number becomes larger than the
largest possible number, no number is possible any more and the computer says
so.

### Input

A single line with the letter `L`, `H` or `C` for every guess of the computer.

### Output

A line `Is it g?` for every attempt, in which $$g$$ is the number the computer
guesses. After the user has answered `C`, one last line `Number of attempts: n`,
in which $$n$$ is the number of guesses the computer needed. If no number is
possible any more, that last line reads `That is impossible!` instead.

### Example

In this session the user was thinking of the number 42.

#### Input:

```
L
L
L
L
H
L
H
C
```

#### Output:

```
Is it 500?
Is it 250?
Is it 125?
Is it 62?
Is it 31?
Is it 46?
Is it 38?
Is it 42?
Number of attempts: 8
```

### Example

In this session the user kept answering that the number to guess is lower, so
in the end no number is possible any more.

#### Input:

```
L
L
L
L
L
L
L
L
L
```

#### Output:

```
Is it 500?
Is it 250?
Is it 125?
Is it 62?
Is it 31?
Is it 15?
Is it 7?
Is it 3?
Is it 1?
That is impossible!
```
