Write a program that picks a random number between 1 and 1000 (you can use
`randint()` for that). The program asks the user to guess the number. After
every attempt of the user, the program says "Lower" if the number to guess is
lower, "Higher" if the number to guess is higher, or "You guessed it!" if the
number is correct. The program ends by printing how many attempts the user
needed to guess the number. For testing purposes it may be smart to show the
number to guess on screen, until you are sure that the program works correctly.

{:class="callout callout-warning"}
> #### Watch out
> Only the lines described below may be printed. If you had your program print the number to guess while testing, remove that again before you submit your solution.

### Input

A sequence of guesses, one integer per line. The program only reads guesses
until the number it picked has been guessed, so any remaining guesses are
ignored.

### Output

A single line for every guess that was read:

- `Lower` if the number to guess is lower than the guess

- `Higher` if the number to guess is higher than the guess

- `You guessed it!` if the guess is the number to guess

After the correct guess, one last line `Number of attempts: n`, in which $$n$$
is the number of guesses the user needed.

### Example

In this session the program had picked the number 42.

#### Input:

```
500
250
125
62
31
46
39
42
```

#### Output:

```
Lower
Lower
Lower
Lower
Higher
Lower
Higher
You guessed it!
Number of attempts: 8
```
