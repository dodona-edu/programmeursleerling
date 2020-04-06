Een **kwadratische vergelijking** is een vergelijking van de vorm 

$$ax^2 + bx + c = 0\,,$$

waarin $$a, b, c \in \mathbb{R}$$ en $$a \neq 0$$.

De grootheid

$$\Delta = b^2 - 4ac$$

wordt de **discriminant** van de kwadratische vergelijking genoemd. Het teken van $$\Delta$$ bepaalt het aantal reële oplossingen:

- als $$\Delta > 0$$ dan zijn er twee verschillende reële oplossingen $$x_1 \neq x_2$$

- als $$\Delta = 0$$ dan zijn er twee gelijke reële oplossingen $$x_1 = x_2$$

- als $$\Delta < 0$$ dan zijn er geen reële oplossingen voor de vergelijking

De reële oplossingen kunnen bepaald worden met de zogenaamde wortelformule:

$$x_{1} = \frac{-b - \sqrt{\Delta}}{2a}\ \ \ \text{en}\ \ \ x_{2} = \frac{-b + \sqrt{\Delta}}{2a}$$

### Opgave

- Schrijf een functie `discriminant` waaraan de drie parameters $$a$$, $$b$$ en $$c$$ (`int` of `float`) van een kwadratische vergelijking moeten doorgegeven worden. De functie moet de discriminant $$\Delta$$ (`float`) van de kwadratische vergelijking teruggeven.

- Schrijf een functie `oplossingen` waaraan de drie parameters $$a$$, $$b$$ en $$c$$ (`int` of `float`) van een kwadratische vergelijking moeten doorgegeven worden. De functie moet drie waarden teruggeven: *i*) het aantal verschillende reële oplossingen (`int`) van de vierkantsvergelijking, *ii*) de oplossing $$x_1$$ (`float`) van de vierkantsvergelijking en *iii*) de oplossing $$x_2$$ (`float`) van de vierkantsvergelijking. Als de kwadratische vergelijking geen reële oplossingen heeft, dan moet de waarde $$0$$ teruggegeven worden voor $$x_1$$ en $$x_2$$.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> discriminant(1, 0, -1)
4.0
>>> discriminant(1, 4, -5)
36.0

>>> oplossingen(1, 0, -1)
(1, -1.0, 1.0)
>>> oplossingen(1, 4, -5)
(1, -5.0, 1.0)
```
