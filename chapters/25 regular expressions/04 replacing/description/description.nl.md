Hoewel gewoonlijk reguliere expressies alleen gebruikt worden om naar
patronen te zoeken, kun je ze ook gebruiken om substrings in een string
te vervangen door andere substrings. Dit doe je met de `sub()` methode.
`sub()` krijgt als argumenten het patroon dat je wilt vervangen, het
patroon waarmee je wilt vervangen, en de string. `sub()` retourneert de
nieuwe string (bedenk dat strings onveranderbaar zijn, dus `sub()` maakt
geen wijziging in de string, zelfs niet als die in een variabele staat;
als je de nieuwe string wilt gebruiken moet je hem zelf in een variabele
stoppen).

De vervanging is meestal gewoon een string, maar er kunnen verwijzingen
in staan naar groepen in het eerste patroon. Je moet dan een formaat
gebruiken dat verschilt van het `\\x` formaat dat ik hierboven
beschreef. Als je wilt refereren aan groep `x` in het patroon (waarbij
`x` een getal is), dan schrijf je `\\g<x>` (ook hier moet je de `<` en
`>` in het patroon opnemen). De reden voor dit verschil is
ondubbelzinnigheid; het maakt het mogelijk om verschil te maken tussen,
bijvoorbeeld, een referentie naar groep 2 gevolgd door het teken 0, en
een referentie naar groep 20.

```python
import re

s = re.sub( r"([iy])z(eert)", "\g<1>s\g<2>", "Of je nu \
categorizeert, rationalizeert, of analyzeert, je moet \
een s gebruiken!" )
print( s )
```
