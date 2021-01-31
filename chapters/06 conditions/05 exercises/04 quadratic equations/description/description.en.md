A **quadratic equation** is any equation that can be rearranged in standard form as 

$$ax^2 + bx + c = 0\,,$$

where $$a, b, c \in \mathbb{R}$$ and $$a \neq 0$$.

The expression

$$\Delta = b^2 - 4ac$$

is called the **discriminant** of the quadratic equation. The sign of $$\Delta$$ determines the number of real-valued solutions:

- if $$\Delta > 0$$, then there are two distinct real-valued solutions ($$x_1 \neq x_2$$)

- als $$\Delta = 0$$, then both real-valued solutions are the same ($$x_1 = x_2$$)

- als $$\Delta < 0$$, then there are no real-valued solutions

The real-valued solutions can be determined as:
 
$$x_{1} = \frac{-b - \sqrt{\Delta}}{2a}\ \ \ \text{en}\ \ \ x_{2} = \frac{-b + \sqrt{\Delta}}{2a}$$

### Input

The three parameters $$a$$, $$b$$ and $$c$$ of a quadratic equation, each on a separate line.

### Output

A line that indicates the number of different real-valued solutions of the quadratic equation. The solutions themselves must also be mentioned (if they exist).

### Example

#### Input:

```
1
4
-5
```

#### Output:

```
Er zijn 2 reële oplossingen: -5.0 en 1.0
```

### Example

#### Input:

```
1
-12
36
```

#### Output:

```
Er is 1 reële oplossing: 6.0
```

### Example

#### Input:

```
4
2
7
```

#### Output:

```
Er zijn geen reële oplossingen
```

### Example

#### Input:

```
0
0
3
```

#### Output:

```
Ongeldige vergelijking
```
