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
