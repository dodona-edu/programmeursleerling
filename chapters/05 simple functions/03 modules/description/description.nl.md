Python biedt basis functies, waarvan ik er een aantal hierboven
besproken heb. Naast die basis functies biedt Python ook een groot
aantal zogeheten "modules," waarin zich vele nuttige functies bevinden.
Om de functies van een module te gebruiken in een programma, moet je de
juiste module importeren door boven in je programma
`import <modulenaam>` op te nemen. Je kunt dan alle functies die in de
betreffende module staan in je programma gebruiken, maar je moet de
functie-aanroepen vooraf laten gaan door de naam van de module en een
punt. Bijvoorbeeld, om de functie `sqrt()` uit de `math` module (die de
wortel van een getal trekt) te gebruiken, roep je `math.sqrt()` aan
nadat je `math` geïmporteerd hebt.

Als alternatief kun je ook specifieke functies vanuit een module
importeren, via:  

```python
from <module> import <functie1>, <functie2>, <functie3>, ...
```
  
Het voordeel van een dergelijke manier van functies importeren is dat je
in je code niet de naam van de module voor de functie-aanroep hoeft te
zetten.

Bijvoorbeeld:

```python
import math

print( math.sqrt( 4 ) )
```

is equivalent aan:

```python
from math import sqrt

print( sqrt( 4 ) )
```

Als je een functie onder een andere naam in je programma wilt gebruiken,
kun je dat doen middels het gereserveerde woord `as`. Dit kan zinvol
zijn als je meerdere modules gebruikt waarin toevallig functies
voorkomen die dezelfde naam hebben.

```python
from math import sqrt as squareroot

print( squareroot( 4 ) )
```

Ik bespreek nu een aantal functies uit twee veelgebruikte standaard
modules, en een aantal functies die in een module staan die ik voor dit
boek gebouwd heb (in hoofdstuk
<a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>
leg ik uit hoe je je eigen modules kunt maken). Er zijn veel meer
standaard modules naast de modules die ik hieronder noem, en sommige
ervan komen later nog aan de orde. Andere zul je zelf moeten opzoeken
als je ze nodig hebt. Je mag er echter van uitgaan dat voor ieder
min-of-meer-algemeen probleem dat je wilt oplossen, er iemand is geweest
die er een module voor ontwikkeld heeft die het eenvoudig of zelfs
triviaal maakt om het probleem op te lossen. Dus in de praktijk geldt:
ga niet meteen zelf coderen, maar zoek eerst even uit of je niet gebruik
kunt maken van de moeite die iemand anders gedaan heeft.

### `math`

De `math` module bevat een aantal nuttige wiskundige functies. Deze
functies zijn meestal zeer efficiënt, en retourneren meestal een float.
Ik noem hier een klein aantal van de functies; als je er meer wilt
kennen kun je ze opzoeken in de Python referentie):

-   `exp()` krijgt één numerieke parameter en retourneert $$e$$ tot de
    macht van die parameter. Als je niet weet wat $$e$$ is: $$e$$ is een
    speciaal getal met veel interessante eigenschappen, en wordt veel
    gebruikt in natuurkunde, wiskunde, en statistiek.

-   `log()` krijgt één numerieke parameter en retourneert het natuurlijk
    logaritme van die parameter. Het natuurlijk logaritme is de waarde
    die de parameter als uitkomst heeft als je $$e$$ verheft tot deze
    waarde. Net als $$e$$ heeft het natuurlijk logaritme toepassingen in
    natuurkunde, wiskunde, en statistiek.

-   `log10()` krijgt één numerieke parameter en retourneert het
    logaritme met 10 als basis van de parameter.

-   `sqrt()` krijgt één numerieke parameter en retourneert de
    vierkantswortel van die parameter.

Bijvoorbeeld:

```python
from math import exp, log

print( "De waarde van e is bij benadering", exp( 1 ) )
e_sqr = exp( 2 )
print( "e kwadraat is", e_sqr, "wat betekent" )
print( "dat log(", e_sqr, ") gelijk is aan", log( e_sqr ) )
```

### `random`

De `random` module bevat functies die pseudo-toevalsgetallen genereren.
Ik zeg "pseudo-toevalsgetallen" en niet "toevalsgetallen," aangezien het
onmogelijk is voor digitale computers om echt toevalsgetallen te
genereren. Maar voor alle toepassingen mag je ervan uitgaan dat deze
module toevalsgetallen genereert.

-   `random()` krijgt geen parameters, en retourneert een toevalsgetal
    als een float binnen het bereik $$[0,1)$$, dat wil zeggen een bereik
    tussen nul en 1, waarbij 0.0 wel meedoet maar 1.0 niet.

-   `randint()` krijgt twee parameters, beide integers, waarbij de
    eerste kleiner dan of gelijk aan de tweede moet zijn. Het
    retourneert een toevalsgetal dat een integer is dat ligt binnen het
    bereik dat begrensd wordt door deze twee parameters, inclusief beide
    parameters. Bijvoorbeeld, `randint(2,5)` retourneert 2, 3, 4, of 5,
    elk met een gelijke kans.

-   `seed()` initialiseert de toevalsgetal generator van Python. Als je
    een lijst van toevalsgetallen wilt hebben die iedere keer hetzelfde
    is voor je programma, kun je dat voor elkaar krijgen door aan het
    begin van je programma `seed()` aan te roepen met een vast getal,
    bijvoorbeeld 0. Dit kan nuttig zijn bij het testen van je programma.
    Als je de generator weer echt toevallige getallen wilt laten
    genereren op een later punt in je programma, kun je `seed()`
    nogmaals aanroepen zonder parameter.

For example:

```python
from random import random, randint, seed

seed()
print( "Een toevalsgetal tussen 1 en 10 is", randint( 1, 10 ) )
print( "Een ander is", randint( 1, 10 ) )
seed( 0 )
print( "3 toevalsgetallen zijn:", random(), random(), random() )
seed( 0 )
print( "Dezelfde 3 zijn:", random(), random(), random() )
```

### `pcinput`

`pcinput` is een module die ik voor dit boek geschreven heb. Je vindt
hem in appendix
<a href="#ch:pcinput" data-reference-type="ref" data-reference="ch:pcinput">31</a>,
en je kunt hem gemakkelijk zelf maken (of eenvoudigweg downloaden via
<http://www.spronck.net/pythonbook>). De module bevat vier handige
functies, die de gebruiker op een veilige manier om specifieke input
vragen. De functies zijn de volgende:

-   `getInteger()` krijgt één string parameter, de prompt, en vraagt de
    gebruiker via die prompt om een integer in te geven. Als de
    gebruiker iets ingeeft wat geen integer is, wordt gevraagd de input
    opnieuw in te geven. De functie eindigt pas als de gebruiker een
    correcte integer heeft ingegeven, en de functie retourneert dan de
    ingegeven waarde als een integer.

-   `getFloat()` krijgt één string parameter, de prompt, en vraagt de
    gebruiker via die prompt om een float in te geven. Als de gebruiker
    iets ingeeft wat geen float is, wordt gevraagd de input opnieuw in
    te geven. De functie eindigt pas als de gebruiker een correcte float
    heeft ingegeven, en de functie retourneert dan de ingegeven waarde
    als een float.

-   `getString()` krijgt één string parameter, de prompt, en vraagt de
    gebruiker via die prompt om een string in te geven. Alles wat de
    gebruiker ingeeft wordt als correct beschouwd. De functie
    retourneert de ingegeven waarde, waarbij spaties voor en na de
    ingegeven tekst verwijderd zijn.

-   `getLetter()` krijgt één string parameter, de prompt, en vraagt de
    gebruiker via die prompt om één letter in te geven. Alleen letters
    van het alfabet zijn acceptabel. Pas als de gebruiker precies één
    letter heeft ingegeven eindigt de functie, en de letter wordt dan
    als een hoofdletter geretourneerd.

Deze functies helpen je dus om code te schrijven die de gebruiker vraagt
om input met een specifiek data type te verstrekken, omdat ze garanderen
dat het programma inderdaad iets binnenkrijgt dat van het gevraagde data
type is. De code geeft geen runtime error als de gebruiker iets anders
ingeeft. De functies zijn niet erg netjes, omdat ze foutmeldingen geven
in het Nederlands als iets fouts ingegeven wordt. Dat betekent dat je
deze functies niet moet gebruiken als je een Engelstalig programma
schrijft (daar heb ik een andere versie van de module voor), maar om
Python te leren zijn deze functies afdoende.

Creëer of download de `pcinput` module, zorg dat hij staat in de folder
waar je je programma's schrijft, en maak dan een Python programma met
onderstaande code. Voer het programma uit en test het door iets in te
geven wat geen integer is.

```python
from pcinput import getInteger

num1 = getInteger( "Geef een geheel getal: " )
num2 = getInteger( "Geef een ander geheel getal: " )

print( num1, "+", num2, "=", num1 + num2 )
```

Vraag de gebruiker om een string in te geven. Gebruik dan die string als
prompt om de gebruiker te vragen een float in te geven.

{:class="callout callout-info"}
> #### Opmerking
> Ik leg niet uit hoe `pcinput` werkt, omdat ik er concepten voor gebruik die pas in hoofdstuk <a href="#ch:exceptions" data-reference-type="ref" data-reference="ch:exceptions">18</a> aan bod komen. Je zult later leren hoe je zelf dit soort functies kunt maken. Je hoeft je vooralsnog niet druk te maken over hoe ze werken, je hoeft ze alleen maar te gebruiken. Dat is de houding die je tegenover de meeste standaardfuncties moet hebben: zolang je maar weet wat ze doen, welke parameters ze nodig hebben, en wat ze retourneren, heeft het geen zin na te denken over hoe ze werken.
