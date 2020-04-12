A complex number is a number of the form
$$a + bi$$, whereby $$a$$ and $$b$$ are constants, and $$i$$ is a special
value that is defined as the square root of -1. Of course, you never try
to actually calculate what the square root of -1 is, as that gives a
runtime error; in complex numbers, you always let the $$i$$ remain. For
instance, the complex number $$3 + 2i$$ cannot be simplified any
further.

Multiplication of two complex numbers $$a + bi$$ and $$c + di$$ is
defined as

$$(a\times c - b\times d) + (a\times d + b\times c)i$$

### Assignment

We represent a complex number as a `tuple` of two numeric values. Write a function `product` that calculates the multiplication of two complex numbers.

### Example

```console?lang=python&prompt=>>>
>>> product((3, 4), (7, 2))
(13, 34)
```
