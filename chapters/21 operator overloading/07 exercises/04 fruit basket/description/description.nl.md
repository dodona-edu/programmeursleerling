Implementeer een class
`Fruitmand`. De `Fruitmand` bevat stukken fruit, en voor ieder stuk
fruit kan het een bepaald aantal hebben. Houd het eenvoudig: sla de
stukken fruit op als een dictionary, waarbij de naam van het fruit als
key wordt gebruikt en het aantal als waarde. Voor deze opgave is er geen
beperking op wat de naam van een stuk fruit mag zijn, iedere string is
acceptabel. Implementeer de `__add__()` methode om een stuk fruit toe te
voegen aan de mand (en het zou een goed idee kunnen zijn om ook de
`__iadd()__` methode te implementeren), en implementeer de `__sub__()`
methode om een stuk fruit te verwijderen (en `__isub__()` wellicht ook).
Implementeer de `__contains__()` methode om te controleren of een
bepaalde fruitsoort in de mand zit. Implementeer ook de `__getitem__()`
methode om te controleren hoeveel er van een fruitsoort in de mand zit,
de `__setitem__()` methode om in één keer de hoeveelheid van een
fruitsoort een waarde te geven, en de `__len__()` methode om vast te
stellen hoeveel verschillende soorten fruit in de mand zitten. Merk op
dat het noodzakelijk is om een key uit de dictionary te verwijderen als
de bijbehorende waarde 0 is.

### Opgave

Definieer een klasse `Fruitmand` waarmee een mand met fruit kan voorgesteld worden. Bij het aanmaken van een fruitmand (`Fruitmand`) mag één optioneel argument doorgegeven worden: een dictionary (`dict`) die de naam van een fruitsoort (`str`) afbeeldt op het aantal stuks (`int`) van die fruitsoort in de mand. Als er geen argument doorgegeven wordt, dan moet een lege mand aangemaakt worden.

Fruitmanden (`Fruitmand`) moeten minstens de volgende bewerkingen ondersteunen:

- De ingebouwde functie `len` moet het aantal verschillende fruitsoorten (`int`) in de mand teruggeven.

- De operator `in` (`fruit in mand`) moet teruggeven of de mand minstens één stuk (`bool`) van de gegeven fruitsoort bevat.

- Indexering van een mand (`mand[fruit]`) moet het aantal stuks (`int`) van de gegeven fruitsoort in de mand teruggeven, of `0` als de mand die fruitsoort helemaal niet bevat.

- Toekenning aan een index (`mand[fruit] = n`) moet het aantal stuks van de gegeven fruitsoort in de mand op $$n$$ zetten. Als $$n \leq 0$$, dan moet de fruitsoort uit de mand gehaald worden.

- De operator `+` (`mand + fruit`) moet een nieuwe fruitmand (`Fruitmand`) teruggeven die één stuk meer van de gegeven fruitsoort bevat. De mand waarop de operator toegepast werd mag niet wijzigen. De operator `+=` (`mand += fruit`) moet één stuk meer van de gegeven fruitsoort in de mand zelf leggen.

- De operator `-` (`mand - fruit`) moet een nieuwe fruitmand (`Fruitmand`) teruggeven die één stuk minder van de gegeven fruitsoort bevat. De mand waarop de operator toegepast werd mag niet wijzigen. De operator `-=` (`mand -= fruit`) moet één stuk van de gegeven fruitsoort uit de mand zelf halen. Als het laatste stuk van een fruitsoort weggehaald wordt, dan moet die fruitsoort uit de mand verdwijnen, en een fruitsoort weghalen die niet in de mand zit mag niets wijzigen.

- Als een fruitmand doorgegeven wordt aan de ingebouwde functies `repr` of `str`, dan moet een string (`str`) teruggegeven worden die leest als een Python expressie waarmee dezelfde mand aangemaakt wordt, met de fruitsoorten in alfabetische volgorde.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> mand = Fruitmand({'mango': 2})
>>> mand
Fruitmand({'mango': 2})
>>> len(mand)
1
>>> mand['mango']
2
>>> mand['kiwi']
0
>>> 'kiwi' in mand
False
>>> mand['kiwi'] = 3
>>> mand + 'kiwi'
Fruitmand({'kiwi': 4, 'mango': 2})
>>> mand
Fruitmand({'kiwi': 3, 'mango': 2})
>>> mand -= 'mango'
>>> mand -= 'mango'
>>> mand
Fruitmand({'kiwi': 3})
>>> mand - 'papaya'
Fruitmand({'kiwi': 3})
>>> len(mand)
1
```
