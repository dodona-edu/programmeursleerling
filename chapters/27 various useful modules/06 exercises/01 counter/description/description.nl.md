Gebruik de `Counter` class om de
vijf meest voorkomende letters in een tekst te tonen, inclusief hun
tellingen.

### Opgave

Schrijf een functie `meest_voorkomende_letters` die een string (`str`) als argument neemt en een lijst van `(letter, aantal)`-tuples teruggeeft voor de vijf meest voorkomende letters in de tekst. Enkel letters tellen mee: tekens die geen letter zijn, moeten genegeerd worden, en er wordt geen onderscheid gemaakt tussen hoofd- en kleine letters (beide versies van eenzelfde letter worden samengeteld, en gerapporteerd als kleine letter). Als twee of meer letters even vaak voorkomen, zet je ze in de volgorde waarin ze het eerst voorkomen in de tekst. Als de tekst minder dan vijf verschillende letters bevat, geef je enkel de letters terug die effectief voorkomen.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> meest_voorkomende_letters('mississippi')
[('i', 4), ('s', 4), ('p', 2), ('m', 1)]
>>> meest_voorkomende_letters('AaAaBbBcCcC')
[('a', 4), ('c', 4), ('b', 3)]
```
