Hoe vaak komt elk woord in een tekst voor?

### Opgave

Een woord in een tekst wordt gedefinieerd als een zo lang mogelijke reeks letters. Alle karakters die geen letter zijn, worden dus beschouwd als scheidingstekens voor woorden. Gevraagd wordt:

- Schrijf een functie `woorden_splitsen` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met de opeenvolgende woorden in het gegeven tekstbestand.

- Schrijf een functie `woorden_tellen` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een dictionary (`dict`) teruggeven, die elk woord in het gegeven tekstbestand afbeeldt op het aantal voorkomens van dat woord in het tekstbestand. De functie mag geen onderscheid maken tussen hoofdletters en kleine letters, en moet woorden in kleine letters gebruiken als sleutels van de dictionary die teruggegeven wordt.

{:class="callout callout-info"}
> #### Opmerking
> Dit is exact dezelfde opgave als de vorige opgave, maar
> verwerk nu zeker de tekst regel voor regel. Dit is iets dat je zou moeten doen
als je een erg lange tekst onder handen hebt.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.txt`](media/data/data.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> woorden_splitsen('data.txt')
['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood', 'He', 'would', 'chuck', 'he', 'would', 'as', 'much', 'as', 'he', 'could', 'And', 'chuck', 'as', 'much', 'as', 'a', 'woodchuck', 'would', 'If', 'a', 'woodchuck', 'could', 'chuck', 'wood']
>>> woorden_tellen('data.txt')
{'how': 1, 'much': 3, 'wood': 3, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}
```
