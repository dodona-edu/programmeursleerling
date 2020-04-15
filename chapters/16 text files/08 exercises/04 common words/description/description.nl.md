Wat zijn de gemeenschappelijke woorden van drie tekstbestanden?

### Opgave

Een woord in een tekst wordt gedefinieerd als een zo lang mogelijke reeks letters. Alle karakters die geen letter zijn, worden dus beschouwd als scheidingstekens voor woorden.

Schrijf een functie `gemeenschappelijke_woorden` waaraan de locaties van drie tekstbestanden (`str`) moeten doorgegeven worden. De functie moet een verzameling (`set`) teruggeven met alle woorden (`str`) die in elk van de drie tekstbestanden voorkomen. De functie mag geen onderscheid maken tussen hoofdletters en kleine letters, en moet woorden in de verzameling in kleine letters voorstellen.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat de tekstbestanden [`data_a.txt`](media/data/data_a.txt){:target="_blank"}, [`data_b.txt`](media/data/data_b.txt){:target="_blank"} en [`data_c.txt`](media/data/data_c.txt){:target="_blank"} zich in de huidige directory bevinden.

```console?lang=python&prompt=>>>
>>> gemeenschappelijke_woorden('data_a.txt', 'data_b.txt', 'data_c.txt')
{'and', 'as', 'he'}
```
