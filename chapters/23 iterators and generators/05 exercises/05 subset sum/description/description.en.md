The "subset sum" problem
asks the question whether a list of integers contains a subset of
integers that, when summed, gives zero as answer. For instance, for the
list \[1, 4, -3, -5, 7\] the answer is "yes," as 1 + 4 - 5 = 0. However,
for the list \[1, 4, -3, 7\] the answer is "no," as there is no subset
of integers that adds up to zero. Write a program that solves the
"subset sum" problem for a list of integers. If there is a solution,
print it; if not, report that there is no solution.

This is a repetition of one of the exercises of Chapter
<a href="#ch:lists" data-reference-type="ref" data-reference="ch:lists">13</a>
(Lists). In that chapter I said that you have to solve the exercise
recursively. However, using the `itertools` module, you can now solve it
without recursion (though I suspect that recursion still is used within
the `itertools` module – you, however, do not have to).
