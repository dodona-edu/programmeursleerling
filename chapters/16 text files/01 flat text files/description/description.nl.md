"Tekstbestanden" of "platte tekstbestanden" zijn bestanden waarin alle
tekens bedoeld zijn om te interpreteren als reguliere tekens, zoals je
ze op een toetsenbord intypt. Bijvoorbeeld, Python programma's zijn
platte tekstbestanden, net als HTML bestanden. Tekstverwerkingsbestanden
(zoals je bijvoorbeeld creëert met Word) zijn echter geen platte
tekstbestanden, en plaatjes zijn dat ook niet. Als je wilt weten of een
bestand een tekstbestand is, dan kun je het proberen te openen in een
teksteditor (bijvoorbeeld IDLE). Als je dat doet en alleen leesbare
tekst ziet, betreft het waarschijnlijk een tekstbestand. Anders wordt
het een "binair bestand" genoemd (binaire bestanden worden besproken in
hoofdstuk
<a href="#ch:binaryfiles" data-reference-type="ref" data-reference="ch:binaryfiles">19</a>).

Tekstbestanden bestaan uit regels tekst. Aan het einde van iedere regel
staat een "newline" symbool, in Python voorgesteld als het teken `"\n"`.
Verschillende besturingssystemen hebben verschillende manieren om dit
teken op te slaan: sommige Windows programma's slaan het op als
"carriage return plus line feed" (`"\r\n"`), terwijl het bij Linux
altijd wordt opgeslagen als een enkele `"\n"`. Zolang je in Python een
bestand benadert als een regulier tekstbestand, zal Python de tekens die
het leest converteren naar de standaard `"\n"`, en vice versa wanneer
het tekens wegschrijft. Dus je hoeft je niet druk te maken om dit soort
verschillen (behalve wanneer je bestanden kopieert naar andere
besturingssystemen).

![ASCII muis](media/asciiMouse.png "ASCII muis"){:width="80%"}

### Handles en pointers

Als je met een bestand werkt in een programma, moet je dat bestand
openen. Het openen van een bestand creëert een zogeheten "handle" of
"file handle." Je kunt een handle zien als een variabele die toegang
biedt tot een bestand. Een handle bevat een "pointer," die een
specifieke plaats in het bestand aanduidt. Die pointer wordt gebruikt
als je leest uit het bestand of schrijft naar het bestand. Bijvoorbeeld,
als je uit een bestand leest, begint het lezen daar waar de pointer
wijst, en gedurende het lezen wordt de pointer verplaatst in het
bestand.

Wanneer je een bestand opent, wordt de pointer op een specifiek punt in
het bestand geplaatst, afhankelijk van de manier waarop het bestand
geopend is. Als je het bestand opent alleen om eruit te lezen, dan staat
de pointer aan het begin. Hetzelfde geldt als je het bestand opent voor
zowel lezen als schrijven. Als je een bestand opent voor "appending"
(dat wil zeggen, om nieuwe data toe te voegen aan het einde van het
bestand), dan staat de pointer aan het einde. Tenslotte, als je het
bestand opent voor alleen schrijven, dan wordt het bestand volledig leeg
gemaakt en wordt de pointer geplaatst aan het begin van het, nu lege,
bestand. Om een nieuw bestand te creëren (dat wil zeggen, een bestand
met een naam die nog niet bestaat), open je het bestand voor alleen
schrijven.

Na het openen van het bestand is de handle het enige toegangspunt tot
het bestand. Alle acties die je uitvoert op het bestand, voer je uit met
behulp van methodes van de handle.

Merk op dat er een restrictie bestaat binnen het besturingssysteem op
het aantal bestanden dat tegelijkertijd geopend mag worden (hoewel deze
restrictie over het algemeen erg hoog ligt). Het is daarom een goed idee
om bestanden te sluiten als je ze niet langer nodig hebt.

### Verplaatsing van de pointer

De pointer, die aangeeft waar je in het bestand bezig bent, wordt
automatisch verplaatst. Bijvoorbeeld, als je 10 tekens uit het bestand
wilt lezen, dan geeft de pointer aan welk de eerste van die 10 tekens
is. Terwijl je leest, verplaatst de pointer zich 10 tekens, zodat de
nieuwe pointer positie 10 tekens verder in het bestand is dan voordat de
leesactie plaatsvond. Als je met tekstbestanden werkt, is deze
automatische verplaatsing van de pointer precies wat je wilt. Er zijn
methodes waarmee je de pointer handmatig kunt verplaatsen, maar zulke
methodes worden over het algemeen alleen gebruikt bij binaire bestanden.
In dit hoofdstuk zal ik daarom deze methodes niet bespreken, maar ik
breng ze aan de orde in hoofdstuk
<a href="#ch:binaryfiles" data-reference-type="ref" data-reference="ch:binaryfiles">19</a>.

### Buffers

Als je wijzigingen maakt in bestanden, dan worden die vaak niet
onmiddellijk in de betreffende bestanden opgeslagen. In plaats daarvan
slaat het besturingssysteem de wijzigingen op in een buffer in het
geheugen, en maakt de wijzigingen pas definitief in het bestand als dat
nodig is (een praktijk die "flushing" wordt genoemd). Je kunt het
definitief maken van de wijzigingen forceren door het bestand te
sluiten. Bestanden worden ook automatisch gesloten als je je programma
op een normale manier beëindigt – maar het is niet zo netjes om het
sluiten niet expliciet in het programma te doen.

Als je programma crasht (bijvoorbeeld vanwege een runtime error), dan
kan het gebeuren dat je wijzigingen niet allemaal zijn opgeslagen, en je
bestanden daarom niet up-to-date zijn tot het moment dat de crash
plaatsvond. Dus als je probeert een programma te debuggen kun je er niet
van uitgaan dat de inhoud van de bestanden zo is als het programma ze
gemaakt zou moeten te hebben.

### Bestandsverwerking

De meeste programma's die bestandsverwerking doen, volgen een proces
dat, in een loop, de inhoud van een bestand leest, die inhoud op een of
andere manier verwerkt, en tenslotte de bewerkte inhoud naar een ander
bestand schrijft. Bijvoorbeeld, een programma kan regels uit een
tekstbestand lezen, de woorden in iedere regel sorteren, en dan de
gesorteerde woorden naar een ander bestand schrijven. Dit verschilt
nauwelijks met een programma dat de gebruiker in een loop vraagt om een
regel tekst, de woorden in de regel sorteert, en die woorden dan op het
scherm toont met de `print()` functie. Ik heb gezien dat studenten het
relatief gemakkelijk vinden om de versie van het programma te schrijven
waarbij de gebruiker met het programma communiceert, maar het erg
moeilijk vinden om een soortgelijk programma te schrijven dat informatie
uit een bestand leest.

Ik ben er nooit achter gekomen waarom zoveel studenten
bestandsverwerking zo lastig vinden, maar ik vermoed dat ze het gevoel
hebben de controle over hun programma te verliezen als ze met bestanden
werken. Als input handmatig verstrekt wordt, en output getoond wordt op
het scherm, dan weet je min of meer welke regels code Python aan het
uitvoeren is, en je kunt testen wat je wilt. Maar als je met bestanden
werkt, dan moet je die bestanden van te voren klaarmaken, en dan het
programma uitvoeren en wachten tot het klaar is voordat je de output
bestanden kunt controleren.

Je hebt misschien het gevoel weinig controle over een bestandsverwerkend
programma te hebben, maar tijdens het bouwen van het programma kun je
altijd `print()` statements in je code opnemen om inzicht te krijgen in
wat het programma doet. Bijvoorbeeld, wanneer je programma een regel uit
een tekstbestand leest, kun je die regel printen, en als je programma
een regel schrijft, kun je die ook printen. Op die manier is het inzicht
dat je krijgt in de werkwijze van je programma nauwelijks anders dan
wanneer je handmatige invoer aan je programma verstrekt.
