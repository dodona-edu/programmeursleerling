The greatest common divider is the greatest
integer that divides two other integers without remainder. For instance,
the greatest common divider of 14 and 21 is 7, as 7 is the greatest
number that divides both 14 and 21.

Euclid's algorithm that calculates
the greatest common divider of two numbers says that if the largest
divided by the smallest is an integer, it is the smallest. Otherwise, it
is the result of calculating the greatest common divider of the smallest
and the remainder of the largest divided by the smallest. This is a
recursive defintion.

### Opgave

Write a recursive function `gcd` that takes two integers $$a, b \in \mathbb{N}$$. The function must return the greatest common divider of $$a$$ and $$b$$, based on an implementation of Euclid's algorithm.

{:class="callout callout-info"}
> #### Tip
> Testing whether two numbers divide each other, and calculating the remainder, can both be done with the modulo operator. This code can be *really* brief.

### Example

```console?lang=python&prompt=>>>
>>> gcd(14, 21)
7
```
