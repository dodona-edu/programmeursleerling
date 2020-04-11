Als je een variabele die een list omvat toekent aan een andere variabele
middels de assignment operator (=), denk je misschien dat je een kopie
hebt gemaakt van de list. Maar dat is niet wat er gebeurt. Je maakt op
deze manier een *alias* voor de list, dat wil zeggen, een nieuwe
variabele die refereert aan precies dezelfde list. Je kunt de nieuwe
variabele gebruiken als een list, maar iedere wijziging die je maakt in
de list waaraan de variabele refereert, is ook te zien is in de list
waaraan de originele variabele refereert, en vice versa. Het zijn niet
twee verschillende lists.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
print( fruitlist )
print( fruitlist2 )
fruitlist2[2] = "mango"
print( fruitlist )
print( fruitlist2 )
```

Iedere variabele in Python heeft een identificatie nummer. Dat nummer
kun je zien met de `id()` functie. Het ID nummer geeft aan welke
geheugenadres door de variabele gebruikt wordt. Voor een alias van een
list is de ID (logischerwijs) hetzelfde als voor de originele list.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
print( id( fruitlist ) )
print( id( fruitlist2 ) )
```

Als je een kopie van een list wilt creëren, kun je dat doen met een
klein truukje. In plaats van `<nieuwlist> = <oudlist>` te gebruiken,
gebruik je `<nieuwlist> = <oudlist>[:]`.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
fruitlist3 = fruitlist[:]

print( id( fruitlist ) )
print( id( fruitlist2 ) )
print( id( fruitlist3 ) )

fruitlist[2] = "mango"
print( fruitlist )
print( fruitlist2 )
print( fruitlist3 )
```

### `is`

Het gereserveerde woord `is` is geïntroduceerd om de identiteiten van
twee variabelen met elkaar te vergelijken.

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
fruitlist3 = fruitlist[:]

print( fruitlist is fruitlist2 )
print( fruitlist is fruitlist3 )
print( fruitlist2 is fruitlist3 )
```

Zoals je kunt zien, weet `is` te bepalen dat `fruitlist` en `fruitlist2`
een alias van elkaar zijn, maar dat `fruitlist3` niet dezelfde list is.
Als je ze echter vergelijkt met de $==$ operator, zijn de resultaten
anders dan als je ze vergelijkt met `is`:

```python
fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
fruitlist3 = fruitlist[:]

print( fruitlist == fruitlist2 )
print( fruitlist == fruitlist3 )
print( fruitlist2 == fruitlist3 )
```

De $==$ operator vergelijkt de inhoud van de lists, dus er wordt `True`
geretourneerd voor alle vergelijkingen. Voor data types waarvoor de $==$
niet speciaal gedefinieerd is, wordt een identiteitsvergelijking
uitgevoerd. Maar voor lists is de $==$ operator gedefinieerd als een
vergelijking van list inhoud. Ik ga dieper op dit onderwerp in als ik
het ga hebben over "operator overloading" in hoofdstuk
<a href="#ch:operatoroverloading" data-reference-type="ref" data-reference="ch:operatoroverloading">22</a>.

### Ondiepe versus diepe kopieën

Als er items op een list voorkomen die zelf lists zijn (of andere
veranderbare data structuren, die in de komende hoofdstukken aan bod
komen), kan het kopiëren van een list middels
`<nieuwlist> = <oudlist>[:]` problemen geven. De reden is dat een
dergelijke kopie een "ondiepe kopie" is. Dat betekent dat de
kopie-operatie ieder element van de list via een reguliere assignment
operator kopieert, wat betekent dat items in de nieuwe list die zelf een
list zijn een alias worden van van de items in de originele list.

```python
numlist = [ 1, 2, [3, 4] ]
copylist = numlist[:]

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

In de code hierboven zie je dat de assignment `numlist[0] = 5` alleen
een wijziging maakt in `numlist`, aangezien `copylist` een (ondiepe)
kopie is van `numlist`. Maar de assignment `numlist[2][0] = 6` maakt een
wijziging in beide lists, omdat de sub-list `[3, 4]` in `copylist`
opgeslagen is als een alias.

Om een "diepe kopie" van een list te maken (dat wil zeggen, een kopie
die ook echte kopieën bevat van alle veranderbare substructuren in de
list, en ook echte kopieën van alle veranderbare substructuren in
veranderbare substructuren in de list, etcetera), kun je de module
`copy` gebruiken. De `deepcopy()` functie van de `copy` module maakt
diepe kopieën van iedere willekeurige veranderbare data structuur. Je
geeft aan de `deepcopy()` functie de te kopiëren data structuur als
argument mee, en je krijgt als retourwaarde een diepe kopie van deze
data structuur.

```python
from copy import deepcopy

numlist = [ 1, 2, [3, 4] ]
copylist = deepcopy( numlist )

numlist[0] = 5
numlist[2][0] = 6
print( numlist )
print( copylist )
```

De `copy` module bevat ook een functie `copy()` die ondiepe kopieën
maakt. Je vraagt je misschien af waarom die functie bestaat; je kunt
immers ook ondiepe kopieën maken met `<nieuwlist> = <oudlist>[:]`. Het
antwoord is dat de `copy` module niet alleen werkt voor lists, maar voor
alle veranderbare data structuren, en voor niet iedere data structuur is
er een truukje als dat voor lists beschikbaar.

### Lists als argumenten

Als je een list aan een functie meegeeft als argument, dan is dit een
zogeheten "pass by reference" ("doorgifte via een referentie" – waarbij
je een referentie kunt beschouwen als een alias). De parameter die de
list bevat, en die een locale variabele voor de functie is, bevat een
alias voor de list die je hebt meegegeven. Dat betekent dat de functie
de inhoud van de list kan wijzigen.

Dit is een belangrijk punt, dus ik herhaal het: als je een veranderbare
data structuur meegeeft als argument aan een functie, dan krijgt de
functie een alias voor de data structuur, en dus kan de inhoud van de
data structuur gewijzigd worden door de functie.

Je moet dus weten of een functie waaraan je een list meegeeft de list
wel of niet zal wijzigen. Als je niet wilt dat de functie de originele
list wijzigt, en je weet niet of de functie dat zal doen, dan moet je
een diepe kopie van de list meegeven aan de functie.

```python
def wijziglist( x ):
    if len( x ) > 0:
        x[0] = "FRUIT!"

fruitlist = ["appel", "banaan", "kers", "doerian"]
wijziglist( fruitlist )
print( fruitlist )
```

De reden dat een list als alias wordt meegegeven, en niet als een diepe
kopie, is dat technisch gezien ieder argument dat een functie meekrijgt
in de computer moet worden opgeslagen in een specifiek stuk geheugen dat
een deel is van de processor. Dit is de "stack," en dit stack geheugen
is niet erg omvangrijk. Omdat lists enorm groot kunnen zijn, zou een
programma dat lists op de stack zet allerlei runtime errors kunnen
veroorzaken. In Python, net als in de meeste andere programmeertalen,
worden alleen de basis data types (zoals integers, floats, en strings)
als waarde aan een functie meegegeven, en alle andere data structuren
als alias.
