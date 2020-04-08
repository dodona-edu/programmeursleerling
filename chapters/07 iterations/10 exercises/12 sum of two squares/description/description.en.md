Which numbers can be written as the sum of two squares?

### Input

Two integers $$m, n \in \mathbb{N}$$, where $$m \leq n$$.

### Output

Each sum of squares ($$x^2 + y^2$$ where $$x \leq y$$) that results in a value from the interval $$[m, n]$$. The output is a list of line that are formatted as

> `x ** 2 + y ** 2 = z`

{:class="callout callout-info"}
> #### Note
> Some numbers can be written as a sum of two squares in multiple ways. The output must contain all of them. 

### Example

#### Input:

```
48
52
```

#### Output:

```
0 ** 2 + 7 ** 2 = 49
1 ** 2 + 7 ** 2 = 50
4 ** 2 + 6 ** 2 = 52
5 ** 2 + 5 ** 2 = 50
```
