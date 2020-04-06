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

### Assignment

- Write a function `discriminant` that takes the three parameters $$a$$, $$b$$ and $$c$$ (`int` or `float`) of a quadratic equation. The function must return the discriminant $$\Delta$$ (`float`) of the quadratic equation.

- Write a function `solutions` that takes the three parameters $$a$$, $$b$$ and $$c$$ (`int` or `float`) of a quadratic equation. The function must return three values: *i*) the number of different real-valued solutions (`int`) of the quadratic equation, *ii*) the solution $$x_1$$ (`float`) of the quadratic equation and *iii*) the solution $$x_2$$ (`float`)  of the quadratic equation. If the quadratic equation has no real-valued solution, the value $$0$$ must be returned for both $$x_1$$ and $$x_2$$.

### Example

```console?lang=python&prompt=>>>
>>> discriminant(1, 0, -1)
4.0
>>> discriminant(1, 4, -5)
36.0

>>> solutions(1, 0, -1)
(1, -1.0, 1.0)
>>> solutions(1, 4, -5)
(1, -5.0, 1.0)
```
