Een "dictionary" (letterlijk: "woordenboek," maar die vergelijking loopt
spaak in Python) is een ongeordende data structuur die een verzameling
elementen bevat. Om een element te vinden, moet je de "key" ("sleutel")
van het element kennen.

In de grond is een dictionary een verzameling van "keys" met
geassocieerde waardes. Ieder onveranderbaar data type mag gebruikt
worden als key. Een veelgebruikt data type dat als key wordt ingezet is
de string.

Dictionaries creëer middels accolades `\{\}`, vergelijkbaar met hoe je
lists creëert met vierkante haken. Een lege dictionary maak je door een
assignment aan een variabele te doen met `\{\}`. Je kunt een dictionary
met inhoud creëren door ieder element dat je erin wilt hebben tussen de
accolades te zetten, met als syntax `<key>:<value>`, en komma's tussen
de elementen.

Hieronder bouw ik een dictionary fruitmand, met drie elementen, namelijk
de key `"appel"` met waarde 3, de key `"banaan"` met waarde 5, en de key
`"kers"` met waarde 50.

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
```

Om een waarde te vinden die hoort bij een specifieke sleutel, gebruik je
dezelfde syntax als voor een list, behalve dat waar je bij een list de
index schrijft, je bij een dictionary de gezochte key schrijft.

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand["banaan"] )
```

Je kunt via een `for` loop een dictionary doorlopen. De variabele in de
`for` loop krijgt de waardes van de keys.

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
for key in fruitmand:
    print( "{}:{}".format( key, fruitmand[key] ))
```

Als je een dictionary element probeert te benaderen met een key die niet
voorkomt in de dictionary, krijg je een runtime error. Maar als je een
nieuw element wilt toevoegen, kun je dat eenvoudigweg doen door een
waarde toe te kennen aan een dictionary element met de nieuwe key.
Bijvoorbeeld, om een `"mango"` toe te voegen aan de `fruitmand`, doe je
het volgende:

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand )
fruitmand["mango"] = 1
print( fruitmand )
```

Op dezelfde wijze kun je een bestaand dictionary element overschrijven.

Om een element te verwijderen uit een dictionary, gebruik je het
gereserveerde woord `del`, net zoals je het gebruikt met lists.

```python
fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand )
del fruitmand["banaan"]
print( fruitmand )
```

Je kunt het aantal elementen in de dictionary bepalen met de `len()`
functie.

Snap je overigens in welke volgorde de dictionary de elementen aanbiedt
als je de inhoud van de dictionary print? Denk er even over na.

Het antwoord is: de volgorde is willekeurig. Ik zei dat bij het begin
van het hoofdstuk: dictionaries zijn ongeordend. Ik kan je niet eens
zeggen wat voor volgorde je op je scherm ziet als een de code hierboven
uitvoert, want de volgorde kan verschillen tussen computers,
besturingssystemen, en versies van Python. Er is een zekere structuur in
de ordening, maar niet een die je zou kunnen (of willen) voorspellen.
Door voldoende nieuwe elementen toe te voegen, kan de volgorde zelfs
plotseling drastisch wijzigen.

Omdat dictionaries ongeordend zijn, zijn vele concepten die gelden voor
lists, niet van toepassing op dictionaries. Bijvoorbeeld, je kunt geen
"subdictionary" maken door een key-bereik te definiëren, je kunt kunt
een dictionary niet "sorteren" of "inverteren." Dictionaries zijn daarom
wat beperkt, maar ze kunnen nuttig zijn.
