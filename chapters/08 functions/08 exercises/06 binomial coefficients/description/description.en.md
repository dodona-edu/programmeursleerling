How many color combinations are possible with a choice of three colors from the seven colors of the rainbow? The order of the colors is not important. There are

$$\binom{7}{3} = \frac{7!}{3!4!} = 35$$

How is this value obtained? There are 7 options for chosing the first color, 6 options for the second color, and 5 options for the third color. So, in total there are $$7 \times 6 \times 5 = \frac{7!}{4!} = 210$$ possibilities.

But this takes into account the order of the colors: it is possible to choose red s the first color followed by yellow as the second color, but also to choose yellow as the first color and red as the second color. To get rid of this order, we have to divide the result by the number of different orderings of the three colors. That is

$$1 \times 2 \times 3 = 3! = 6$$

### Assignment

The **factorial** of a positive integer $$n$$, denoted by $$n!$$, is the product of all positive integers less than or equal to $$n$$:

$$n! = \prod_{k=1}^{n}k = 1 \times 2 \times 3 \times \cdots \times n$$

For example, if $$n = 5$$ then

$$5! = 1 \times 2 \times 3 \times 4 \times 5 = 120$$

According to the convention for an empty product, we have that

$$0! = 1$$

A **binomial coefficients**, denoted by

$$\binom{n}{k}$$

and read as "$$n$$ choose $$k$$", is a value used in combinatorics to indicate the number of ways to choose an (unordered) subset of $$k$$ elements from a fixed set of $$n$$ elements. Such a choice is called a **combination**. A binomial coefficient is defined as the positive integer

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}\ \ \ \text{for }0 \leq k \leq n$$

and

$$\binom{n}{k} = 0\ \ \ \text{for }k < 0\text{ or }k > n$$

Your task:

- Write a function `factorial` that takes an integer $$n \in \mathbb{N}$$ (`int`). The function must return $$n!$$ (`int`).

- Write a function `binomial` that takes two integers $$n, k \in \mathbb{N}$$ (`int`). The function must return $$\binom{n}{k}$$.

### Example

```console?lang=python&prompt=>>>
>>> factorial(5)
120

>>> binomial(7, 3)
35
```
