De manier waarop de rij van Fibonacci gedefinieerd is, is een voorbeeld van wat in de wiskunde een **recursieve definitie** genoemd wordt. De rij begint met 0 en 1 en vervolgens is elk volgende element van de rij steeds de som van de twee voorgaande elementen. Het $$n$$-de getal van Fibonacci $$F_n$$ wordt zo gegeven door:

$$F_0 = 0,\ \ \ F_1 = 1$$

en

$$F_n = F_{n-1} + F_{n-2}$$

voor $$n > 1$$.

Het begin van de reeks is dus

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

### Opgave

Om meer inzicht te krijgen in hoe recursie werkt: pas de functie `fib` aan door er een diepte-parameter aan toe te voegen, die start met nul en die met 1 verhoogd wordt iedere keer dat een diepere versie van de functie wordt aangeroepen. Bij binnenkomst van de functie druk je het nummer af waarmee de functie wordt aangeroepen, en als er een waarde wordt geretourneerd, druk je ook die waarde af. Gebruik de diepte parameter om de afgedrukte waardes in te springen (tweemaal zoveel spaties als de diepte). 

{:class="callout callout-info"}
> #### Observatie
> Bestudeer de output. Denk je dat het een goed idee is om de
Fibonacci reeks recursief te implementeren? Waarom, of waarom niet?

### Voorbeeld

```console?lang=python&prompt=>>>
>>> fib(5, 0)
fib(5, 0)
  fib(4, 1)
    fib(3, 2)
      fib(2, 3)
        fib(1, 4)
        return 1
        fib(0, 4)
        return 0
      return 1
      fib(1, 3)
      return 1
    return 2
    fib(2, 2)
      fib(1, 3)
      return 1
      fib(0, 3)
      return 0
    return 1
  return 3
  fib(3, 1)
    fib(2, 2)
      fib(1, 3)
      return 1
      fib(0, 3)
      return 0
    return 1
    fib(1, 2)
    return 1
  return 2
return 5
5
```
