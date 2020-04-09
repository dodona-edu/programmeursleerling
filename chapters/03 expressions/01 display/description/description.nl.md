Als je een expressie schrijft in de Python shell, en hem uitvoert, wordt
het resultaat van de expressie eronder getoond. Bijvoorbeeld, als je het
volgende commando in de shell schrijft en op `Enter` drukt, zie je het
resultaat $$12$$.

```python
5 + 7
```

Echter, zoals ik liet zien in opgave
<a href="#python.shell" data-reference-type="ref" data-reference="python.shell">[python.shell]</a>,
als je een programma schrijft dat alleen het commando `5 + 7` bevat, dan
zie je geen resultaat. In plaats daarvan moet je voor programma's altijd
expliciet aangeven dat je resultaten wilt tonen, zelfs als het gaat om
een commando dat op de laatste regel van het programma staat.

Ook al gaat dit hoofdstuk over expressies, ik moet toch eerst iets
uitleggen dat geen expressie is, maar een functie, namelijk een functie
die het mogelijk maakt resultaten te laten zien. De functie die dat doet
is `print`. Ik heb deze functie al gebruikt in hoofdstukken
<a href="#ch:introduction" data-reference-type="ref" data-reference="ch:introduction">2</a>
en
<a href="#ch:usingpython" data-reference-type="ref" data-reference="ch:usingpython">3</a>.

De `print` functie gebruik je als volgt: je schrijft het woord `print`,
gevolgd door een rond openingshaakje, gevolgd door hetgeen je wilt laten
zien, gevolgd door een rond sluithaakje. Bijvoorbeeld (en ook dit
commando heb ik meerdere malen laten zien):

```python
print( "Hello, world!" )
```

Als je deze code draait (door het op te slaan in een Python bestand en
het te draaien in IDLE), zie je dat de tekst "Hello, world!" in de shell
wordt getoond.

Overigens is het gebruikelijk dat wanneer auteurs van teksten over
programmeren een functie bij naam noemen, ze er een openings- en
sluithaakje achter zetten, om aan te geven dat het een functienaam
betreft. Vanaf nu zal ik dat ook doen. Bovendien gebruiken auteurs soms
niet het woord "functie," maar het woord "statement" of "commando." Deze
termen duiden echter meestal op alles wat Python kan uitvoeren, niet
alleen functies. Bijvoorbeeld, een expressie is ook een "commando."

Je kunt meerdere dingen tegelijkertijd laten zien met een `print()`
functie, door alles wat je wilt laten zien tussen de haakjes te zetten,
met komma's ertussen. De `print()` functie laat dan al die items zien,
met spaties ertussen. Bijvoorbeeld:

```python
print( "Ik", "heb", "twee", "appels", "en", "een", "banaan" )
```

De spaties in dit commando zijn overigens overbodig.

```python
print("Ik","heb","twee","appels","en","een","banaan")
```

is precies hetzelfde als het commando ervoor. Je kunt zulke spaties
toevoegen om de leesbaarheid te vergroten. Je mag ook spaties zetten
tussen het woord `print` en het openingshaakje, maar de gewoonte is om
bij functies altijd het openingshaakje aan de naam van de functie "vast
te plakken."

Merk op dat je met `print()` niet alleen teksten, maar ook getallen kunt
laten zien. Je mag zelfs teksten en getallen door elkaar gebruiken.

```python
print( "Ik", "heb", 2, "appels", "en", 1, "banaan" )
```

Laat een paar teksten zien met behulp van een Python programma. Let erop
dat je alle teksten tussen aanhalingstekens moet plaatsen; je mag naar
keuze dubbele of enkele aanhalingstekens gebruiken.
