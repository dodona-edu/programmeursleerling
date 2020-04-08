A prime number is a positive integer that is divisible by exactly two different
numbers, namely 1 and itself. The lowest (and only even) prime number is 2. The
first 10 prime numbers are 

> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### Input

An integer $$n \in \mathbb{N}_0$$.

### Output

A sentence that indicates if $$n$$ is a prime.

{:class="callout callout-info"}
> #### Tip
> In a loop where you test the possible dividers of the number, you can conclude that the number is not prime as soon as you encounter a number other than 1 or itself that divides it. However, you can only conclude that it actually is prime after you have tested all possible dividers.

### Example

#### Input:

```
11
```

#### Output:

```
11 is a prime
```

### Example

#### Input:

```
12
```

#### Output:

```
11 is not a prime
```
