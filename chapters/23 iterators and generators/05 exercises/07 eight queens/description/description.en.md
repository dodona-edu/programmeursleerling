Write a program that
determines how you can place eight queens on a chess board in such a way
that none of them attacks any of the other ones. This is a classic
problem that sounds like it has little to do with this chapter, but when
you consider that you may solve it using the `permutations()` function
in a smart way, you will find that this program can be surprisingly
short.

### Assignment

Write a generator function `queens` that takes an optional integer
`number` (`int`), which defaults to `8`. The function must `yield` every
solution for placing `number` queens on a `number` × `number` chess
board so that no queen attacks another.

Each solution is represented as a tuple of length `number`. The value at
index $$i$$ of the tuple is the (0-based) column of the queen placed on
row $$i$$. For example, the tuple `(1, 3, 0, 2)` means that the queen on
row 0 is in column 1, the queen on row 1 is in column 3, the queen on
row 2 is in column 0, and the queen on row 3 is in column 2.

The order in which the solutions are yielded does not matter.

### Example

```console?lang=python&prompt=>>>
>>> len(list(queens()))
92

>>> sorted(queens(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
```
