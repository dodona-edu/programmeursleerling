Tel hoe vaak iedere letter voorkomt in een
string (zonder verschil te maken tussen hoofd- en kleine letters). Je
mag ieder teken dat geen letter is negeren. Print de letters met het
aantal malen dat ze voorkomen, waarbij je de letters sorteert van veel
voorkomend naar weinig voorkomend.

### Opgave

Schrijf een functie `tel_letters` waaraan een string (`str`) moet doorgegeven worden. De functie moet afdrukken hoe vaak elke letter voorkomt in de gegeven string, met één letter per regel, telkens de letter gevolgd door een dubbelpunt, een spatie en het aantal keer dat ze voorkomt. Maak daarbij geen onderscheid tussen hoofd- en kleine letters, en druk de letters af als kleine letters. Tekens die geen letter zijn, moeten genegeerd worden. Druk de letters af van veel naar weinig voorkomend, en zet letters die even vaak voorkomen alfabetisch.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> tel_letters('Hello, World!')
l: 3
o: 2
d: 1
e: 1
h: 1
r: 1
w: 1
>>> tel_letters('12345 + 67890 = ?')
```
