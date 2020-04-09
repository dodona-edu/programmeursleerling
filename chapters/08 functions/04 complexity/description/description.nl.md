Stel dat Python geen ingebouwde functies `max()` en `min()` zou hebben,
en je hebt geen kennis van wat er in de hoofdstukken hierna volgt. Ik
geef je de volgende opdracht:

Schrijf een programma dat twee groepen van drie getallen krijgt (je mag
het programma schrijven voor specifieke getallen, maar je voegt later
toe dat de gebruiker deze getallen ingeeft). Het programma telt de
waardes van de kleinste getallen van iedere groep op, en ook zo voor de
waardes van de middelste getallen, en de waardes van de grootste
getallen. Daarna drukt het de uitkomsten af.

Hoe los je dit op? Je kunt beginnen met iets als:

```python
# Eerst krijgen de variabelen in groep 1 (num11, num12, num13) en
# groep 2 (num21, num22, num23) een waarde.

kleinste1 = 0
kleinste2 = 0
middelste1 = 0
middelste2 = 0
grootste1 = 0
grootste2 = 0

if num11 < num12:
    if num11 < num13:
        kleinste1 = num11
    else:
        kleinste1 = num13
elif num12 < num13:
    kleinste1 = num12
else:
    kleinste1 = num13

print( kleinste1 ) # Test

# Deze code zoekt de kleinste van groep 1.
# Daarna doe je hetzelfde voor de kleinste van groep 2.
# Dan moet je ook zoiets doen voor de grootste van de 2 groepen.
# Daarna moet je nog iets verzinnen voor de middelste.
# Tenslotte doe je alle optellingen en drukt de resultaten af.
```

Je kunt je voorstellen dat deze aanpak, met geneste `if` statements die
zes keer herhaald worden met verschillende assignments in de takken,
leidt tot een behoorlijk groot, onleesbaar, onbeheersbaar programma
waarvan het lastig te zien is of het correct is of niet. Je moet het
probleem op een slimmere manier aanpakken.

Stel je voor dat je een functie hebt die de kleinste van drie getallen
bepaalt, een functie die de middelste van drie getallen bepaalt, en een
functie die de grootste van drie getallen bepaalt. Dan is het programma
triviaal geworden. Het is dan iets als:

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def kleinste( n1, n2, n3 ):
    return n1 # Geef iets terug

def middelste( n1, n2, n3 ):
    return n1 # Geef iets terug

def grootste( n1, n2, n3 ):
    return n1 # Geef iets terug

print( "som van kleinste =", kleinste( num11, num12, num13 ) + 
    kleinste( num21, num22, num23 ) )
print( "som van middelste =", middelste( num11, num12, num13 ) + 
    middelste( num21, num22, num23 ) )
print( "som van grootste =", grootste( num11, num12, num13 ) + 
    grootste( num21, num22, num23 ) )
```

{:class="callout callout-info"}
> #### Opmerking
> In de code hierboven heb ik een meervoudige assignment gebruikt om de variabelen `num`$$xx$$ een waarde te geven, om de lengte van de code te reduceren. Hierbij kun je in één statement meerdere variabele een waarde geven door links van het is-gelijk-teken een aantal variabelen te zetten, en rechts ervan evenveel waardes. De eerste waarde gaat naar de eerste variabele, de tweede waarde naar de tweede variabele, etcetera. Dit wordt verder uitgelegd in hoofdstuk <a href="#ch:tuples" data-reference-type="ref" data-reference="ch:tuples">12</a>.

Het programma hierboven is leesbaar, begrijpbaar, en kan al getest
worden. Natuurlijk, de functies `kleinste()`, `middelste()`, en
`grootste()` retourneren niet de correcte waardes. Misschien weet je
zelfs nog niet eens hoe je ze zou moeten implementeren. Maar je voelt
waarschijnlijk wel aan dat ze geïmplementeerd kunnen worden, en je weet
dat je de code voor deze functies later kunt schrijven, en in kleine
stapjes.

Hoe implementeer je `kleinste()`? Zoals ik boven liet zien is het lastig
om dit met een geneste `if` te doen (als je dat niet gelooft, kijk dan
niet naar mijn code en probeer het zelf te schrijven; het blijkt
moeilijk te zijn om de variabelen in gedachten te houden terwijl je de
geneste `if` schrijft). Kan dit misschien op een wat leesbaardere manier
gedaan worden?

Is het lastig om de kleinste van twee getallen te retourneren? Nee, dat
is heel gemakkelijk:

```python
def kleinste_van_twee( n1, n2 ):
    if n1 < n2:
        return n1
    return n2
```

Door een dergelijke functie te nesten, kun je de een `kleinste()`
functie maken die de kleinste van drie getallen bepaalt. Dat kun je ook
doen voor `grootste()`. Het programma wordt dan:

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def kleinste_van_twee( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def grootste_van_twee( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def kleinste( n1, n2, n3 ):
    return kleinste_van_twee( kleinste_van_twee( n1, n2 ), n3 )

def middelste( n1, n2, n3 ):
    return n1 # geef iets terug

def grootste( n1, n2, n3 ):
    return grootste_van_twee( grootste_van_twee( n1, n2 ), n3 )

print( "som van kleinste =", kleinste( num11, num12, num13 ) + 
    kleinste( num21, num22, num23 ) )
print( "som van middelste =", middelste( num11, num12, num13 ) + 
    middelste( num21, num22, num23 ) )
print( "som van grootste =", grootste( num11, num12, num13 ) + 
    grootste( num21, num22, num23 ) )
```

Dit programma werkt voor de kleinste getallen en de grootste getallen.
Om het af te maken, moet nog iets bepaald worden voor de middelste. Wat
is het middelste van drie getallen? Dat is het getal dat overblijft als
je de kleinste en de grootste weghaalt. Kun je dit programmeren? Ik stel
een functie `verwijder_twee_van_drie()` voor, die eerst de kleinste,
en dan de grootste van de twee overgebleven getallen verwijdert (wat
weer gelijk is aan de eerder bepaalde grootste). Om
`verwijder_twee_van_drie()` gemakkelijk te kunnen bouwen, maak ik ook
`verwijder_een_van_drie()` en `verwijder_een_van_twee()`.

```python
num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def kleinste_van_twee( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def grootste_van_twee( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def verwijder_een_van_drie( n1, n2, n3, verwijder ):
    if n1 == verwijder:
        return n2, n3
    elif n2 == verwijder:
        return n1, n3
    return n1, n2

def verwijder_een_van_twee( n1, n2, verwijder ):
    if n1 == verwijder:
        return n2
    return n1

def verwijder_twee_van_drie( n1, n2, n3, verwijder1, verwijder2):
    num1, num2 = verwijder_een_van_drie( n1, n2, n3, verwijder1 )
    return verwijder_een_van_twee( num1, num2, verwijder2 )

def kleinste( n1, n2, n3 ):
    return kleinste_van_twee( kleinste_van_twee( n1, n2 ), n3 )

def middelste( n1, n2, n3 ):
    return verwijder_twee_van_drie( n1, n2, n3, 
        kleinste( n1, n2, n3 ), grootste( n1, n2, n3 ) )

def grootste( n1, n2, n3 ):
    return grootste_van_twee( grootste_van_twee( n1, n2 ), n3 )

print( "som van kleinste =", kleinste( num11, num12, num13 ) + 
    kleinste( num21, num22, num23 ) )
print( "som van middelste =", middelste( num11, num12, num13 ) + 
    middelste( num21, num22, num23 ) )
print( "som van grootste =", grootste( num11, num12, num13 ) + 
    grootste( num21, num22, num23 ) )
```

Het programma is nu klaar en het werkt. Het is best lang, maar alle
functies zijn gemakkelijk te begrijpen, en het is ook niet moeilijk om
te zien hoe het programma als geheel werkt. Het is nog steeds een stuk
korter dan de allereerste poging, met zes geneste `if` statements, en
het is een stuk leesbaarder.

Er zijn natuurlijk andere manieren om het programma aan te pakken. Met
een beetje inventiviteit kom je waarschijnlijk op slimmere manieren om
de kleinste, middelste, en grootste te bepalen (ik ben nog niet echt
tevreden over mijn aanpak van de middelste). Maar het programma werkt en
is begrijpbaar, en dat is het belangrijkste.

Je kunt de aanpak die ik gekozen heb bekritiseren. Bijvoorbeeld, de
berekening van de kleinste van de drie wordt twee keer uitgevoerd: de
eerste keer om de kleinste te bepalen, en de tweede keer om de middelste
te bepalen. Dat geldt ook voor de grootste. Kan dat geoptimaliseerd
worden, zodat deze bepalingen slechts één keer plaatsvinden? Natuurlijk
kan dat, bijvoorbeeld door twee extra variabelen op te nemen die de
kleinste en grootste bijhouden. Maar waarom zou ik dat doen? Dat maakt
het programma niet leesbaarder, en hoewel het het programma een beetje
sneller maakt, spreken we daarbij over nanoseconden. Voor een programma
als dit is snelheid niet belangrijk en volledig ondergeschikt aan
leesbaarheid. Laat me nogmaals benadrukken dat het oplossen van een
probleem op de eerste plaats komt, onmiddellijk gevolgd door het
oplossen van het probleem op een leesbare en beheersbare manier.
Efficiëntie komt pas veel later.

Wat je hiervan moet leren is dat als een programma bestaat uit een serie
problemen die je moeilijk op kunt lossen, je het moet proberen op te
splitsen in sub-problemen en sub-doelen, die je onafhankelijk van elkaar
kunt aanpakken. Je kunt voor ieder van die sub-problemen alvast een
functie introduceren als je het programma opzet, en voorlopig vul je die
dan met iets simpels, bijvoorbeeld het retourneren van een vaste waarde.
Je kunt dan in ieder geval je programma al testen. Later kun je dan
beginnen met het één-voor-één invullen van ieder van die functies.
