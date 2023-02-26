Middels de operatoren die ik heb uitgelegd, kun je de inhoud van
variabelen zo vaak wijzigen in je code als je nodig hebt. Je kunt nieuwe
waardes in bestaande variabelen stoppen. Vaak wil je dat inderdaad doen.
Bijvoorbeeld, het komt in code vaak voor dat er 1 moet worden opgeteld
bij een numerieke variabele (waarom dat zo vaak voorkomt zul je zien in
hoofdstuk
8).
Omdat dit zo vaak gebeurt, bevat Python een aantal "verkorte notaties"
om de inhoud van variabelen aan te passen.

De volgende code:

```python
aantal_bananen = 100
aantal_bananen = aantal_bananen + 1
print( aantal_bananen )
```

is hetzelfde als:

```python
aantal_bananen = 100
aantal_bananen += 1
print( aantal_bananen )
```

Het verschil is de tweede regel. Als je iets wilt optellen bij een
variabele, kun je `+=` gebruiken als assignment operator, met de
variabele aan de linkerkant en wat je erbij op wilt tellen aan de
rechterkant. Dit bespaart de moeite van het twee keer typen van de
variabele naam, en maakt je code over het algemeen leesbaarder (omdat
programmeurs ervan uitgaan dat je de `+=` operator gebruikt als je
ergens iets bij wilt optellen).

Op vergelijkbare manier kun je `-=` gebruiken om iets af te trekken van
een variabele, `*=` voor vermenigvuldiging, `/=` voor deling, `**=` voor
machtsverheffing, etcetera. De meeste verkorte versies worden weinig
gebruikt, behalve `+=`, die juist heel veel gebruikt wordt, en `-=`, die
zo nu en dan gebruikt wordt.

Wat toont de code hieronder? Controleer of je gelijk hebt.

```python
aantal_bananen = 100
aantal_bananen += 12
aantal_bananen -= 13
aantal_bananen *= 19
aantal_bananen /= aantal_bananen
print( aantal_bananen )
```
