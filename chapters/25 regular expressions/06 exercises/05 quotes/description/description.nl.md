Als een persoon spreekt, dan wordt dit in een stuk tekst meestal weergegeven door de gesproken tekst tussen dubbele aanhalingstekens (`"`) te plaatsen.

### Opgave

Schrijf een functie `citaten` waaraan de locatie van een tekstbestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met alle citaten in de gegeven tekst. Hierbij is een citaat een fragment dat tussen dubbele aanhalingstekens geplaatst werd.

{:class="callout callout-info"}
> #### Tip
> Gebruik groepen en bedenk dat reguliere expressies "gulzig" zijn.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.nl.txt`](media/data/data.nl.txt){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> citaten('data.nl.txt')
['Pythonesque']
```
