The "subset sum" problem asks the question
whether a list of integers contains a subset of integers that, when
summed, gives zero as answer. For instance, for the list
`[1, 4, -3, -5, 7]` the answer is "yes," as $1 + 4 - 5 = 0$. However,
for the list `[1, 4, -3, 7]` the answer is "no," as there is no subset
of integers that adds up to zero. Write a program that solves the
"subset sum" problem for a list of integers. If there is a solution,
print it; if not, report that there is no solution.

Hint: This problem is tackled best using recursion. If you skipped
Chapter
10,
you better skip this exercise too.

### Assignment

Write a function `subset_sum` that takes a list (`list`) of integers (`int`). The function must return a list (`list`) that contains a subset of the given integers that adds up to zero. That subset must contain at least one integer, and cannot use any integer more often than it occurs in the given list. If no such subset exists, the function must return `None`.

There may be more than one subset that adds up to zero. In that case the function may return any one of them.

### Example

```console?lang=python&prompt=>>>
>>> subset_sum([1, 4, -3, -5, 7])
[1, 4, -5]
>>> subset_sum([1, 4, -3, 7])
>>> subset_sum([17, -4, -4, -4, -4, -1])
[17, -4, -4, -4, -4, -1]
```
