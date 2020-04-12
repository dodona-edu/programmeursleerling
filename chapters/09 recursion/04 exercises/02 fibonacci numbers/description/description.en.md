In mathematics, the **Fibonacci numbers**, commonly denoted $$F_n$$, form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

$$F_0 = 0,\ \ \ F_1 = 1$$

and

$$F_n = F_{n-1} + F_{n-2}$$

for $$n > 1$$.

The beginning of the sequence is thus:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

### Assignment

To get a bit more insight into how
recursion works, add a depth parameter to the function `fib` from
the previous exercise, that starts at zero and gets increased by 1 for
every deeper call. On entry of the function, print with what number
argument it was called, and when returning a value, print what you
return. Use the depth parameter to indent the prints (twice the number of spaces as the depth). 

{:class="callout callout-info"}
> #### Observation
> Study your output. Do you think it is a good idea to implement the Fibonacci sequence recursively? Why or why not? 


### Example

```console?lang=python&prompt=>>>
>>> fib(5, 0)
fib(5, 0)
  fib(4, 1)
    fib(3, 2)
      fib(2, 3)
        fib(1, 4)
        return 1
        fib(0, 4)
        return 0
      return 1
      fib(1, 3)
      return 1
    return 2
    fib(2, 2)
      fib(1, 3)
      return 1
      fib(0, 3)
      return 0
    return 1
  return 3
  fib(3, 1)
    fib(2, 2)
      fib(1, 3)
      return 1
      fib(0, 3)
      return 0
    return 1
    fib(1, 2)
    return 1
  return 2
return 5
5
```
