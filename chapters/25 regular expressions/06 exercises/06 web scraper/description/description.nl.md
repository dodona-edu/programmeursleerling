Als je data wilt halen uit HTML pagina's, zoek je vaak naar de delen waarin je geïnteresseerd bent middels "mark-ups." Stel dat je een pagina hebt met data van personen, die een ID en een naam hebben. De ID is een negen-cijferig getal, omsloten door een code `<id>` ervoor, en een code `</id>` erna. De naam van de persoon volgt onmiddellijk na de ID, en wordt gemarkeerd door de code `<name>` ervoor, en de code `</name>` erna.

### Opgave

Schrijf een functie `webscraper` waaraan de locatie van een HTML-bestand (`str`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met de gegevens van alle personen uit het bestand. De gegevens van een persoon worden voorgesteld als een `tuple` met de ID (`int`) en de naam (`str`) van de persoon.

### Voorbeeld

In onderstaande interactieve sessie gaan we ervan uit dat het tekstbestand [`data.html`](media/data/data.html){:target="_blank"} zich in de huidige directory bevindt.

```console?lang=python&prompt=>>>
>>> webscraper('data.html')
[(123123123, 'Groucho Marx'), (123123124, 'Harpo Marx'), (123123125, 'Chico Marx'), (123123126, 'Zeppo Marx'), (123123127, 'Gummo Marx')]
```
