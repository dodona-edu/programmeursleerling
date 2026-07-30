A **quadratic equation** is any equation that can be rearranged in standard form as 

$$ax^2 + bx + c = 0\,,$$

where $$a, b, c \in \mathbb{R}$$ and $$a \neq 0$$.

The expression

$$\Delta = b^2 - 4ac$$

is called the **discriminant** of the quadratic equation. The sign of $$\Delta$$ determines the number of real-valued solutions:

- if $$\Delta > 0$$, then there are two distinct real-valued solutions ($$x_1 \neq x_2$$)

- if $$\Delta = 0$$, then both real-valued solutions are the same ($$x_1 = x_2$$)

- if $$\Delta < 0$$, then there are no real-valued solutions

The real-valued solutions can be determined as:
 
$$x_{1} = \frac{-b - \sqrt{\Delta}}{2a}\ \ \ \text{and}\ \ \ x_{2} = \frac{-b + \sqrt{\Delta}}{2a}$$

### Input

The three parameters $$a$$, $$b$$ and $$c$$ of a quadratic equation, each on a separate line.

### Output

A line that indicates the number of different real-valued solutions of the quadratic equation. The solutions themselves must also be mentioned (if they exist). If $$a = 0$$, the given parameters do not describe a quadratic equation, and the output must be `Invalid equation`.

### Example

#### Input:

```
1
4
-5
```

#### Output:

```
There are 2 real-valued solutions: -5.0 and 1.0
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
There is 1 real-valued solution: 6.0
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
There are no real-valued solutions
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
Invalid equation
```
