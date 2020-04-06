De [Grerory-Leibnitz reeks](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80){:target="_blank"} benadert $$\pi$$ op basis van de reeksontwikkeling

$$4 \times \left(\frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots\right)$$

### Opgave

Schrijf een functie `gregory_leibnitz` waaraan een getal $$n \in \mathbb{N}_0$$ (`int`) moet doorgegeven worden. De functie moet de benadering (`float`) van $$\pi$$ teruggeven die men bekomt op basis van de eerste $$n$$ termen van de Grerory-Leibnitz reeks.

### Voorbeeld

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
