De volledige naam van een persoon bestaat uit twee of meer woorden, die elkaar opvolgen, en die alleen letters van het alfabet bevatten die allemaal kleine letters zijn behalve de eerste, die een hoofdletter moet zijn. Tussen de woorden mogen alleen spaties staan. De woorden beginnen en eindigen bij een woordscheider. Volgens deze specificatie is bijvoorbeeld Kardinaal Richelieu een naam, maar Charles  d'Artagnan niet, noch Gilbert duPrez, Joe DiMaggio, of Unit X1138.

### Opgave

Schrijf een functie `namen` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met alle vermoedelijke namen die in het gegeven tekstbestand voorkomen. Hierbij is een vermoedelijke naam een combinatie van twee of meer opeenvolgende woorden die voldoet aan de beschijving uit de inleiding.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.nl.txt`](media/data/data.nl.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> namen('data.nl.txt')
['Monty Python', 'Flying Circus', 'Graham Chapman', 'John\nCleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Monty Python', 'Holy Grail', 'The Meaning', 'Noord Amerika', 'Saturday Night']
```
