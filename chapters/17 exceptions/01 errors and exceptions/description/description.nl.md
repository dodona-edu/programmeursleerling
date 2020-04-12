Als je een Python programma start, controleert Python eerst of alle
statements in je programma voldoen aan de syntax-eisen die Python stelt.
Als dat niet het geval is, genereert Python een zogeheten "syntax error"
en wordt het programma niet uitgevoerd. Als Python geen syntax errors
tegenkomt, wordt het programma uitgevoerd, maar er kunnen dan nog steeds
statements gevonden worden die fouten genereren als ze worden
uitgevoerd. Zulke statements veroorzaken een "runtime error." Je hebt
runtime errors regelmatig gezien tijdens het ontwikkelen en testen van
programma's (ontken het maar niet).

Over het algemeen zul je proberen runtime errors op te lossen door je
code uit te breiden of te wijzigen. Bijvoorbeeld, het volgende programma
geeft een runtime error als je nul ingeeft:

```python
from pcinput import getInteger

num = getInteger( "Geef een getal: " )
print( "3 gedeeld door {} is {}".format( num, 3/num ) )
print( "Tot ziens!" )
```

Python vertelt je wat voor soort error het is, namelijk een
`ZeroDivisionError`. Om die op te lossen, kun je het programma wijzigen:

```python
from pcinput import getInteger

num = getInteger( "Geef een getal: " )
if num == 0:
    print( "Je kunt niet delen door nul" )
else:
    print( "3 gedeeld door {} is {}".format( num, 3/num ) )
print( "Tot ziens!" )
```

`ZeroDivisionError` is de naam van een "exception" die Python
genereert.[^21] Als je een exception niet afhandelt in je programma,
breekt Python de uitvoering van het programma af en smijt een
foutmelding op het scherm. Dit houdt in dat je ervoor zou kunnen zorgen
dat het programma gewoon verder doorloopt, als je er maar voor zorgt dat
de exception afgehandeld wordt.

In de code hierboven zou je ervoor moeten zorgen dat er nimmer een
exception wordt gegenereerd omdat door nul gedeeld wordt – aangezien je
kunt voorzien dat dat zou kunnen gebeuren. Het gebeurt echter wel eens
dat je zult moeten accepteren dat exceptions kunnen optreden omdat je
gewoonweg niet alle omstandigheden waarin je programma wordt uitgevoerd
kunt voorzien. Dat is specifiek het geval als je programma afhangt van
zaken die je niet onder controle kunt hebben, zoals bij het werken met
bestanden en gebruikershandelingen.

[^21]: In het Engels heet dit "raising an exception." `raise` is een
    gereserveerd woord in Python, dat iets later in dit hoofdstuk
    besproken wordt.
