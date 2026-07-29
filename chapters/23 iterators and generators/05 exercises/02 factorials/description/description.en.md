Create a generator that
produces factorials. The first value returned is $1!$, the second $2!$,
the third $3!$, etcetera, up to $10!$. Do not calculate the factorial
every time from scratch, but retain the value that you used in the
previous cycle and use that.

### Assignment

Write a **generator** function `factorials` that takes one optional
argument `count` (`int`), defaulting to `10`. The generator yields
$1!, 2!, 3!, \ldots$ up to and including `count`$!$, in that order. If
`count` is `0`, the generator yields nothing.

As explained above, each yielded value must be derived from the
previous one (by multiplying it with the next integer), rather than
recomputing the factorial from scratch every time.

### Example

```console?lang=python&prompt=>>>
>>> list(factorials())
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

>>> list(factorials(5))
[1, 2, 6, 24, 120]

>>> list(factorials(0))
[]
```
