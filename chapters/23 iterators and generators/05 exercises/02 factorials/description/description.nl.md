Schrijf een generator die
faculteiten produceert. De eerste waarde die geretourneerd wordt is
$1!$, de tweede $2!$, de derde $3!$, etcetera, tot en met $10!$. Bereken
niet iedere keer de faculteit opnieuw, maar bewaar het laatst verkregen
getal en gebruik dat om het volgende te berekenen.

### Opgave

Schrijf een **generator**-functie `faculteiten` die één optioneel
argument `aantal` (`int`) meekrijgt, met als standaardwaarde `10`. De
generator produceert $1!, 2!, 3!, \ldots$ tot en met `aantal`$!$, in die
volgorde. Als `aantal` gelijk is aan `0`, produceert de generator niets.

Zoals hierboven uitgelegd, moet elke geproduceerde waarde afgeleid
worden van de vorige (door die te vermenigvuldigen met het volgende
getal), in plaats van telkens opnieuw de faculteit te berekenen.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> list(faculteiten())
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

>>> list(faculteiten(5))
[1, 2, 6, 24, 120]

>>> list(faculteiten(0))
[]
```
