In mathematics, the **Fibonacci numbers**, commonly denoted $$F_n$$, form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

$$F_0 = 0,\ \ \ F_1 = 1$$

and

$$F_n = F_{n-1} + F_{n-2}$$

for $$n > 1$$.

The beginning of the sequence is thus:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

### Assignment

Write a recursive function `fib` that takes an integer $$n \in \mathbb{N}$$ . The function must return the $$n$$-th Fibonacci number $$F_n$$.

### Example

```console?lang=python&prompt=>>>
>>> fib(0)
0
>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
```
