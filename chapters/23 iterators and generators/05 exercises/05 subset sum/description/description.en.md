The "subset sum" problem
asks the question whether a list of integers contains a subset of
integers that, when summed, gives zero as answer. For instance, for the
list \[1, 4, -3, -5, 7\] the answer is "yes," as 1 + 4 - 5 = 0. However,
for the list \[1, 4, -3, 7\] the answer is "no," as there is no subset
of integers that adds up to zero. Write a program that solves the
"subset sum" problem for a list of integers. If there is a solution,
print it; if not, report that there is no solution.

This is a repetition of one of the exercises of Chapter
13
(Lists). In that chapter I said that you have to solve the exercise
recursively. However, using the `itertools` module, you can now solve it
without recursion (though I suspect that recursion still is used within
the `itertools` module – you, however, do not have to).

### Assignment

"Print one solution" is hard to check automatically, since a list can have
several correct solutions. So instead, write a **generator function**
`zero_subsets` that takes one argument: a list of distinct integers. The
function must `yield` every non-empty subset of the list whose elements sum
to zero, as a `tuple` containing the elements in the same relative order as
in the input list. The empty subset is never yielded, even though it
trivially sums to zero (it is not a solution to the original problem). The
order in which the different subsets are produced does not matter.

### Example

```console?lang=python&prompt=>>>
>>> sorted(zero_subsets([1, 4, -3, -5, 7]))
[(1, -3, -5, 7), (1, 4, -5)]

>>> sorted(zero_subsets([1, 4, -3, 7]))
[]
```
