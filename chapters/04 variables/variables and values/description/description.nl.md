Een variabele is een plaats in het geheugen van de computer die een naam
heeft gekregen, en waarin je een waarde kunt opslaan. De naam mag je
zelf kiezen, en wordt over het algemeen de "variabele naam" genoemd.

Om een variabele te creëren in Python (dus om een variabele naam te
kiezen) moet je een waarde "toekennen" aan gekozen naam middels het
is-gelijk (`=`) symbool. Aan de linkerkant van het is-gelijk symbool zet
je de variabele naam, en aan de rechterkant de waarde die je wilt
opslaan in de variabele. Dit kan ik het beste uitleggen aan de hand van
een voorbeeld:

```python
x = 5
print( x )
```

In deze code gebeuren twee dingen. Ten eerste wordt er een variabele
gecrëerd met de naam `x` door er een waarde in op te slaan, in dit geval
de waarde 5. In het Engels heet dit een "assignment", en het is-gelijk
teken wordt ook wel de "assignment operator" genoemd. Ten tweede wordt
de inhoud van de variabele `x` op het scherm getoond middels `print()`.
Merk op dat `print( x )` niet de letter `x` toont, maar de waarde die in
de variabele `x` is opgeslagen.

![variabele](media/box.png "variabele"){:data-caption="Een variabele kan je voorstellen als een doos waarop je met een dikke, zwarte viltstift een naam hebt geschreven, zodat je hem later gemakkelijk kunt terugvinden. Je kunt iets in de doos stoppen, en je kunt in de doos kijken om te zien wat er in zit (er kan wel slechts één ding tegelijkertijd in de doos zitten). Je kunt aan de inhoud van de
doos refereren door de naam te gebruiken die je op de doos hebt geschreven." width="35%"}

Je kunt je de variabele `x` voorstellen als een doos waarop je met een
dikke, zwarte viltstift een `x` hebt geschreven, zodat je hem later
gemakkelijk terug kunt vinden. Je kunt iets in de doos stoppen, en je
kunt in de doos kijken om te zien wat er in zit (er kan wel slechts één
ding tegelijkertijd in de doos zitten). Je kunt aan de inhoud van de
doos refereren door de naam te gebruiken die je op de doos hebt
geschreven. De term "variabele" duidt op de variabele naam, dus de
letter `x` op de doos. De term "waarde" duidt op de waarde die is
opgeslagen in de variabele, dus de inhoud van de doos.

Aan de rechterkant van het is-gelijk teken kun je alles plaatsen wat een
waarde oplevert. Het hoeft niet een enkel getal te zijn. Het mag ook een
berekening zijn, of een string, of een aanroep van een functie die een
waarde oplevert (bijvoorbeeld de `int()` functie).


<div class="callout callout-info">
  <h4>Opgave</h4>
  <p>In het vorige hoofdstuk was er een oefenopgave die je het aantal
seconden in een week liet uitrekenen. Kopieer die berekening in een
programma, en ken hem toe aan een variabele. Druk dan de variabele af.</p>
</div>

De eerste keer in je programma dat je een waarde toekent aan een
specifieke variabele naam, wordt de bijbehorende variabele gecreëerd.
Als je later een andere waarde aan dezelfde variabele toekent, wordt de
eerste waarde "overschreven." In de metafoor van de doos: je maakt de
doos leeg en stopt er iets nieuws in. Een variabele bevat altijd de
laatst-verkregen waarde.

```python
x = 5
print( x )
x = 7 * 9 + 13   # overschrijft de vorige waarde van x
print( x )
x = "En nu iets heel anders..."
print( x )
x = int( 15 / 4 ) - 27
print( x )
```

Als een variabele is aangemaakt (en dus een waarde heeft) kun je hem
overal in je code gebruiken waar je waardes gebruikt. Je kunt
bijvoorbeeld de variabele gebruiken in een berekening.

```python
x = 2
y = 3
print( "x =", x )
print( "y =", y )
print( "x * y =", x * y )
print( "x + y =", x + y )
```

Je kunt de inhoud van een variabele kopiëren in een andere variabele,
via de assignment operator.

```python
x = 2
y = 3
print( "x =", x, "en y =", y )

# Verwissel de waardes van x en y via z
z = x
x = y
y = z
print( "x =", x, "en y =", y )
```

Als je een waarde toekent aan een variabele, mag je zelfs de variabele
zelf gebruiken aan de rechterkant van de toekenning, zolang de variabele
maar bestaat op het moment dat je dat doet. De rechterkant van een
assignment wordt altijd geheel geëvalueerd voordat de toekenning
plaatsvindt.

```python
x = 2
print( x )
x = x + 3
print( x )
```

Merk op dat de variabele gecreëerd moet zijn voordat je hem kunt
gebruiken. De volgende code geeft een fout, omdat `dagen_per_jaar` nog
niet gecreëerd is voordat hij gebruikt wordt in de eerste regel:

```python
print( dagen_per_jaar )
dagen_per_jaar = 365
```