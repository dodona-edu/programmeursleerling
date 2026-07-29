Create a program that asks the
user to enter positive integers. The user can enter as many as desired,
and indicates that the last integer was entered by supplying zero. The
program the prints all numbers between 1 and 100 that are not divisible
by any of the integers entered. Print those numbers in a
`for ... in ...` loop, using an iterator to produce the numbers.

### Assignment

Write a **generator function** `not_divisible` that takes one argument, a
list of positive integers (`divisors`). The function must **yield** every
integer from 1 up to and including 100 that is not divisible by any of the
integers in `divisors`, in increasing order.

Since `not_divisible` is a generator function, calling it does not
immediately compute anything: it returns an iterator that produces the
numbers one by one, on demand, exactly as in the `for ... in ...` loop
described above.

### Example

```console?lang=python&prompt=>>>
>>> g = not_divisible([2, 3])
>>> next(g)
1
>>> next(g)
5
>>> next(g)
7

>>> list(not_divisible([1]))
[]
```
