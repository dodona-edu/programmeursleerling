Hoe vaak komt elk woord in een tekst voor?

### Opgave

Schrijf een functie `woorden_tellen` waaraan een string (`str`) moet doorgegeven worden. De functie moet een dictionary (`dict`) teruggeven, die elk woord uit de gegeven tekst afbeeldt op het aantal voorkomens van dat woord in de tekst. Hierbij wordt een woord gedefinieerd als de langst mogelijke reeks letters (alle karakters die geen letter zijn, worden dus beschouwd als scheidingstekens voor woorden). De functie mag geen onderscheid maken tussen hoofdletters en kleine letters, en moet woorden in kleine letters gebruiken als sleutels van de dictionary die teruggegeven wordt.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> tekst = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much as a woodchuck would If a woodchuck could chuck wood.'
>>> woorden = woorden_tellen(tekst)
>>> woorden['wood']
>>> woorden['chunck']
```
