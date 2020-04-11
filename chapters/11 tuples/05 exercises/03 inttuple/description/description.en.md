Consider the definition of a new datatype.
The new datatype is the `inttuple`. An `inttuple` is defined as being
either an integer, or a tuple consisting of `inttuple`s. You see an
example of an `inttuple` in the code block below.

```console?lang=python&prompt=>>>
>>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
```

### Assignment

Write a function `flatten` that takes an `inttuple`. The function must return a `tuple` containing all integer values stores in the given `inttuple`.

{:class="callout callout-info"}
> #### Tip
> Since the `inttuple` is defined recursively, a recursive function is probably the
right approach. If you skipped Chapter <a href="#ch:recursion" data-reference-type="ref" data-reference="ch:recursion">10</a>, you probably should skip this exercise too. Use the `isinstance()` function (explained in Chapter <a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>) to determine whether you are dealing with an integer or a tuple.

### Example

```console?lang=python&prompt=>>>
>>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
>>> flatten(inttuple)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
```
