A complex number is a number of the form
$$a + bi$$, whereby $$a$$ and $$b$$ are constants, and $$i$$ is a special
value that is defined as the square root of -1. Of course, you never try
to actually calculate what the square root of -1 is, as that gives a
runtime error; in complex numbers, you always let the $i$ remain. For
instance, the complex number $$3 + 2i$$ cannot be simplified any
further.

Addition of two complex numbers $$a + bi$$ and $$c + di$$ is
defined as

$$(a + c) + (b + d)i$$

### Assignment

We represent a complex number as a `tuple` of two numeric values. Write a function `sum` that calculates the addition of two complex numbers.[^8]

### Example

```console?lang=python&prompt=>>>
>>> sum((3, 4), (7, 2))
(10, 6)
```
