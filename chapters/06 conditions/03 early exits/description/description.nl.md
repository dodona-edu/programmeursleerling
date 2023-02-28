Soms wil je een programma vroegtijdig beëindigen onder bepaalde
condities. Bijvoorbeeld, je programma vraagt de gebruiker om een waarde,
en voert met die waarde een aantal berekeningen uit. Als de gebruiker
een waarde invoert die niet in de berekeningen gebruikt kan worden, wil
je het programma meteen beëindigen. Dat kun je als volgt coderen:

```python
from pcinput import getInteger

num = getInteger( "Geef een positief geheel getal: " )
if num < 0:
    print( "Je had een positief geheel getal moeten geven!" )
else:
    print( "Ik handel je getal", num, "af" )
    print( "Nog meer code" )
    print( "Honderden regels code" )
```

Het is irritant dat een groot deel van het programma al één inspringing
diep staat, terwijl je er de voorkeur aan zou hebben gegeven als het
programma gestopt was na de foutmelding, en de rest van het programma
zonder inspringing geschreven zou kunnen worden. Je kunt dat regelen met
behulp van de functie `exit()` die in de module `sys` staat. De code is
dan:

```python
from pcinput import getInteger
from sys import exit

num = getInteger( "Geef een positief geheel getal: " )
if num < 0:
    print( "Je had een positief geheel getal moeten geven!" )
    exit()

print( "Ik handel je getal", num, "af" )
print( "Nog meer code" )
print( "Honderden regels code" )
```

Als je deze code uitvoert en een negatief getal ingeeft, kan het
gebeuren dat je ziet dat Python een `SystemExit` melding genereert, die
eruit ziet als een grote, lelijke fout. Dit is afhankelijk van de editor
die je gebruikt (IDLE geeft deze melding niet). Het is geen fout, ook al
ziet het er zo uit. Deze melding zegt alleen dat je het programma
geforceerd beëindigd hebt, maar dat is precies wat je wilde doen. Je mag
dit beschouwen als een nette manier van afbreken.

In principe moet je meldingen van Python over je programma niet negeren,
maar deze is een uitzondering. Je mag je programma op deze manier
afbreken. In hoofdstuk
9
zal ik een andere manier van programma afbreken bespreken, die ervoor
zorgt dat je deze melding niet krijgt. Dat kun je tegen die tijd
gebruiken (als de melding je echt stoort), maar vooralsnog moet je hem
maar accepteren.
