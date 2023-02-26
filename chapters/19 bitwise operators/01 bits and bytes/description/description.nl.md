Een bit is de kleinste data-eenheid die een computer kan manipuleren.
Een enkele bit kan slechts twee verschillende waardes aannemen, namelijk
1 en nul.

Hoewel "prehistorische" computers inderdaad geprogrammeerd werden door
direct enen en nullen te manipuleren, werden al snel computers
geïntroduceerd die groepjes bits behandelden. De kleinste eenheid wat
dat betreft is de "byte," die bestaat uit 8 bits. Vandaag de dag worden
computertalen nog steeds afgesteld op het behandelen van bytes, hoewel
de meeste computers tegenwoordig grotere hoeveelheden bytes
tegelijkertijd manipuleren (het meest gebruikelijk zijn computers die
32-bits of 64-bits data-eenheden gebruiken).

### Binair tellen

Een byte bestaat uit 8 bits, die je kunt tonen als een serie enen en
nullen, bijvoorbeeld `11010010`. Op deze manier kan een byte een getal
in binaire code representeren. Als een byte een positief geheel getal
voorstelt, kun je dat getal berekenen door de meest rechtse bit met 1 te
vermenigvuldigen, de bit ernaast met 2, de bit daarnaast met 4,
etcetera, en al dit waardes bij elkaar op te tellen. Bijvoorbeeld, het
binaire getal `11010010` is `1*128+1*64+0*32+1*16+0*8+0*4+1*2+0*1`, wat
210 is. Merk op dat dit equivalent is met het berekenen van de waardes
van decimale getallen, waarbij het rechtse cijfer vermenigvuldigd wordt
met 1, het cijfer ernaast met 10, het cijfer daarnaast met 100,
etcetera, en dan alle uitkomsten worden opgeteld. Het is ook equivalent
met het hexadecimaal tellen, dat ik besprak in hoofdstuk
11.

Als de bits genummerd worden, is het de gewoonte om de meest rechtse bit
van een binair getal nummer nul te geven, en de nummering te laten
toenemen naar links; dus de rechterbit is nummer 0, de bit ernaast
nummer 1, de bit daarnaast nummer 2, etcetera. De reden is dat de
rechterbit de waarde $$2^0$$ representeert (wat gelijk is aan 1), de bit
ernaast de waarde $$2^1$$, de bit daarnaast $$2^2$$, etcetera.

|                         |       |          |        |          |        |        |          |        |       |
|:------------------------|------:|---------:|-------:|---------:|-------:|-------:|---------:|-------:|:------|
| Byte                    |      1|         1|       0|         1|       0|       0|         1|       0|       |
| Nummer van de bit       |      7|         6|       5|         4|       3|       2|         1|       0|       |
| Gerepresenteerde waarde |  $$2^7$$|     $$2^6$$|   $$2^5$$|     $$2^4$$|   $$2^3$$|   $$2^2$$|     $$2^1$$|   $$2^0$$|       |
| Byte waarde             |  $$2^7$$|  \+ $$2^6$$|  \+ $$0$$|  \+ $$2^4$$|  \+ $$0$$|  \+ $$0$$|  \+ $$2^1$$|  \+ $$0$$| = 210 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Schrijf een programma dat van een binaire string, die bestaat uit 8 enen
en nullen, berekent welk decimaal getal erdoor gerepresenteerd wordt. De
mooiste oplossing gebruikt een loop, een vermenigvuldigingsfactor, en
een totaal. Het totaal start bij 0. De vermenigvuldigingsfactor begint
bij 1, en wordt met 2 vermenigvuldigd iedere keer dat de loop doorlopen
wordt. De loop doorloopt de string van rechts naar links (of de
omgekeerde string van links naar rechts). Als een teken gevonden wordt
dat een "1" is, telt het de vermenigvuldigingsfactor op bij het totaal.
Dit geeft uiteindelijk het gevraagde getal.

Het laagste getal dat een byte kan representeren is $$00000000$$, wat
gelijk is aan nul. Het hoogste is $$11111111$$, wat gelijk is aan 255. Er
zijn dus 256 verschillende waardes die door een byte gerepresenteerd
kunnen worden.

### Codering van tekens

De meest basale manier om tekens te coderen is via de ASCII tabel, die
ik toonde in hoofdstuk
11.
In die tabel staan ook voor alle tekens de hexadecimale codes. Het is je
wellicht opgevallen dat de codes liepen van (hexadecimaal) 20 tot en met
7E. De codes onder de 20 worden gebruikt voor speciale controle tekens
(zoals de "newline"). Code 7F wordt gewoonlijk gebruikt om de `Del`
toets te representeren. Andere codes worden niet gebruikt, wat betekent
dat alle ASCII tekens middels 7 bits kunnen worden weergeven, ofwel de
8-bit sequenties $$00000000$$ tot en met $$01111111$$.

Hoewel computers de byte gebruiken als de basis manier om data vast te
leggen, gebruikt ASCII slechts 128 van de 256 tekens die in een byte
zouden kunnen worden opgeslagen. De 128 byte codes die niet door ASCII
worden gebruikt, hebben alle een 1 als de linkerbit. Het ligt voor de
hand dat er teken coderingen zijn die een teken toekennen aan alle 256
waardes die een byte kan bevatten. Een typische manier van zo'n codering
is `latin-1`, die ik in hoofdstuk
17
noemde. Helaas gebruiken niet alle coderingen dezelfde tekens voor byte
waardes 128 tot en met 255. Maar alle manieren van codering die vandaag
de dag in gebruik zijn hebben wel dezelfde basis ASCII tekens in de byte
waardes 0 tot en met 127.

Python is gebaseerd op de Unicode codering. Meer specifiek gebruikt het
UTF-8 als coderingsmechanisme (die ik eerder noemde in hoofdstukken
11
en
17).
UTF-8 werkt als volgt:

-   Een byte die een 0 heeft als meest linker bit is een ASCII teken.

-   Een byte die een 1 heeft als meest linker bit is de start van een
    sequentie van meerdere bytes die samen één teken representeren. De
    sequentie bestaat uit een "leidende byte" (de meest linker byte) en
    één of meer "volgende bytes."

-   Bij een multi-byte sequentie leeft de "leidende byte," van links
    naar rechts, een aantal bits met waarde 1, gevolgd door een bit met
    waarde 0, gevolgd door een aantal resterende bits. De totale lengte
    van de multi-byte sequentie is het aantal bits met waarde 1 links
    van de meest linkse 0 in de leidende byte. Bijvoorbeeld, als de
    leidende byte de waarde $$1110xxxx$$ heeft (waarbij iedere $$x$$ een
    byte is), dan is de hele multi-byte sequentie drie bytes in lengte.
    Dit is inclusief de leidende byte. De minimum lengte van de
    sequentie is twee bytes, en de maximum lengte is zes bytes (in dat
    laatste geval is de leading byte $$1111110x$$).

-   Iedere "volgende byte" heeft 10 als de meeste linkse twee bits.

-   In de praktijk is UTF-8 codering beperkt to een maximum van 4-byte
    sequenties, en sommige van de 4-byte sequenties zijn uitgesloten.

Dit alles betekent dat UTF-8 een zeer groot aantal verschillende tekens
kan representeren. De wijze van coderen betekent ook dat sommige
bit-patronen geen UTF-8 tekens representeren. Hoewel ieder bitpatroon
een legale string in `latin-1` codering is, is het mogelijk om
bitpatronen te construeren die geen legale UTF-8 coderingen zijn.
Hierdoor kunnen die vervelende `UnicodeDecodeError`s ontstaan bij het
lezen van tekstbestanden.

### Coderen van getallen

De manier waarop getallen als bitpatronen zijn opgeslagen is wat
merkwaardig, maar over het algemeen hoef je je daar niet druk om te
maken. Je moet weten dat positieve gehele getallen altijd gecodeerd zijn
als multi-byte patronen, die een 0 als meest linkerbit hebben. De rest
van het patroon is zoals je zou verwachten, en zoals ik hierboven heb
uitgelegd.

Negatieve getallen zijn echter op een andere manier gecodeerd. Ze
gebruiken het zogenaamde "twee-complement systeem." Om een negatief
geheel getal te coderen, neem je eerst de absolute waarde van dat getal
(dat wil zeggen, de positieve versie). Van dat getal neem je het
bitpatroon, en "flipt" alle bits, met andere woorden, je maakt een 1 van
iedere 0, en een 0 van iedere 1. Tenslotte tel je numeriek 1 op bij het
resulterende bitpatroon. Daardoor heeft een bitpatroon dat een negatief
getal representeert altijd een 1 als de meest linkerbit.

Bijvoorbeeld, om $$-1$$ te coderen neem je eerst het bitpatroon van 1, dus
…$$00000001$$. Je flipt alle bits, wat je …$$11111110$$ geeft. Tenslotte
tel je 1 op bij het resultaat, wat …$$11111111$$ oplevert. Dus $$-1$$
wordt gecodeerd als een sequentie van alleen maar enen.

Wat betreft gebroken getallen: die worden opgeslagen in de
wetenschappelijke notatie, waarbij een deel van het multi-byte patroon
als exponent gebruikt wordt.

De reden dat ik dit alles uitleg, is om aan te geven dat als je met
bitpatronen in Python gaat spelen, en je die patronen als getallen
behandelt, je het beste kunt werken met alleen positieve integers, omdat
de bitpatronen van die getallen gemakkelijk geïnterpreteerd kunnen
worden.
