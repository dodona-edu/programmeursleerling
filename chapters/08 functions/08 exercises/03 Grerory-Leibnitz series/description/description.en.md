The [Grerory-Leibnitz series](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80){:target="_blank"} approximates $$\pi$$ using the alternate series

$$4 \times \left(\frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots\right)$$


### Assignment

Write a function `gregory_leibnitz` that takes an integer $$n \in \mathbb{N}_0$$ (`int`). The function must return the approximation for $$\pi$$ obtained from the first $$n$$ terms in the Grerory-Leibnitz series.


### Example

```console?lang=python&prompt=>>>
>>> gregory_leibnitz(1)
4.0
>>> gregory_leibnitz(10)
3.0418396189294032
>>> gregory_leibnitz(100)
3.1315929035585537
>>> gregory_leibnitz(1000)
3.140592653839794
```