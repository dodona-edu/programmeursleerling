`"\n"` is een "speciaal teken" (in het Engels heet dit een "escape
sequence"). Speciale tekens in Python worden over het algemeen
geschreven als een backslash gevolgd door een code. De code kan één of
meerdere tekens beslaan. Python interpreteert zulke speciale tekens, als
ze in een string staan, niet letterlijk.

Naast het "newline" teken `"\n"`, heb ik in hoofdstuk
<a href="#ch:expressions" data-reference-type="ref" data-reference="ch:expressions">4</a>
ook de speciale tekens `"\'"` en `"\""` geïntroduceerd, die je kunt
gebruiken om een enkel respectievelijk dubbel aanhalingsteken in een
string op te nemen, ongeacht het type aanhalingstekens dat je om de
string heen hebt gezet. Ik heb ook genoemd dat je `"\\"` kunt gebruiken
om een "echte" backslash in de string op te nemen.

Naast deze zijn er nog diverse andere speciale tekens. De meeste zijn
behoorlijk archaïsch en worden niet meer gebruikt op moderne computers,
dus die kun je negeren. De twee die ik nog wil noemen zijn `"\t"` die
een tabulatie (inspringing) in de string representeert, en `"\x`$nn$`"`
waarbij $nn$ staat voor twee hexadecimale cijfers, die het hexadecimale
getal $nn$ representeren. Bijvoorbeeld, `"\x20"` is het teken dat
gerepresenteerd wordt door het hexadecimale getal 20, dat hetzelfde is
als het decimale getal 32, wat een spatie is (dit leg ik later in dit
hoofdstuk verder uit).

Voor het geval je nooit hebt geleerd hoe je moet tellen met hexadecimale
getallen: Hexadecimale getallen gebruiken 16 verschillende cijfers,
namelijk 0 tot en met 9 en A tot en met F. Een directe vertaling van
hexadecimale cijfers naar decimale getallen stelt dat A gelijk is aan
10, B aan 11, etcetera. In decimale getallen wordt de waarde van een
getal dat uit meerdere cijfers bestaat berekend door de cijfers te
vermenigvuldigen met oplopende machten van 10, van rechts naar links;
bijvoorbeeld, het getal $1426$ is $6 + 2*10 + 4*100 + 1*1000$. Voor
hexadecimale getallen doe je hetzelfde, maar vermenigvuldig je de
cijfers met oplopende machten van 16; bijvoorbeeld, het hexadecimale
getal $4AF2$ is $2 + 15*16 + 10*256 + 4*4096$. Programmeurs gebruiken
graag hexadecimale getallen, omdat computers als kleinste rekeneenheid
de "byte" gebruiken, en een byte kan 256 verschillende waardes bevatten;
met andere woorden, een byte kan iedere waarde bevatten die je kunt
uitdrukken met precies twee hexadecimale cijfers.

Waarom het nuttig kan zijn te weten hoe je hexadecimaal moet tellen en
waarom je tekens in een string hexadecimaal zou willen representeren
volgt later in dit boek.
