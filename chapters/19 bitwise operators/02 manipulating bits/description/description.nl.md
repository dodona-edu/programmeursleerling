Python biedt een aantal operatoren die de manipulatie van data items op
het niveau van bits toestaan. Dit zijn de volgende:

| operator | betekenis |
|:--------:|:----------|
| `<<` | shift links |
| `>>` | shift rechts |
| `&` | bitsgewijze and |
| `|` | bitsgewijze or |
| `~` | bitsgewijze not |
| `^` | bitsgewijze exclusieve or |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Ze worden als volgt gebruikt.

### Shift

Als je een data item hebt, kun je de `<<` en `>>` operatoren gebruiken
om de bits naar links of naar rechts te verschuiven. `x<<y` verschuift
de bits van `x` `y` posities naar links, waarbij het bitpatroon aan de
rechterkant met 0-bits wordt aangevuld. `x>>y` verschuift de bits van
`x` `y` posities naar rechts, waarbij aan de linkerkant de meest links
bit iedere keer gekopieerd wordt, en de bits aan de rechterkant
verwijderd worden. `x` en `y` moeten beide getallen zijn.

Bijvoorbeeld, het uitroepteken (`\`!) heeft decimale code 33, die je
binair schrijft als $$00100001$$. Als je dit patroon één positie naar
links verschuift, krijg je $$01000010$$, wat decimaal 66 is, en wat de
code is voor de hoofdletter B. Je kunt de verschuiving ongedaan maken
door het bitpatroon voor B één positie naar rechts te verschuiven.

```python
code = "!"
print( chr(ord(code)<<1) )
code = "B"
print( chr(ord(code)>>1) )
```

Het valt je misschien op dat het verschuiven van een bitpatroon van een
getal met één positie naar links neerkomt op het verdubbelen van het
getal, terwijl het verschuiven van één positie naar rechts neerkomt op
het halveren van het getal (waarbij naar beneden wordt afgerond). En
inderdaad is het zo dat het verdubbelen van een getal gelijk is aan het
plaatsen van een 0 aan de rechterkant van het bitpatroon, terwijl het
halveren gelijk is aan het verwijderen van de rechterbit.

```python
print( "345 verviervoudigd levert", 345<<2 )
print( "345 gedeeld door 8 levert", 345>>3 )
```

### Bitsgewijze `and`

De bitsgewijze `and` operator (`&`) neemt twee bitpatronen, en
produceert een nieuw bitpatroon dat bestaat uit alleen maar nullen,
behalve op de posities waar beide originele bitpatronen een 1 hebben,
die in het resultaat dan ook een 1 zijn. Bijvoorbeeld, als de originele
patronen het getal 11 ($$00001011$$) en het getal 6 ($$00000110$$) zijn, dan
geeft de bitsgewijze `and` operator het patroon $$00000010$$, wat het
getal 2 representeert.

```python
print( 11 & 6 )
```

De bitsgewijze `and` is een gemakkelijke manier om een positief getal
modulo een macht van 2 te nemen. Bijvoorbeeld, als je een getal modulo
16 wilt nemen, is dat gelijk aan het toepassen van een bitsgewijze `and`
met 15, wat $$00001111$$ is. Controleer dat 345 modulo 32 gelijk is aan
`345 & 31`.

### Bitsgewijze `or`

De bitsgewijze `or` operator (`|`) neemt twee bitpatronen, en produceert
een nieuw bitpatroon dat bestaat uit alleen maar enen, behalve op de
posities waar beide originele bitpatronen een 0 hebben, die dan ook in
het resultaat een 0 zijn. Bijvoorbeeld, als de originele patronen het
getal 11 ($$00001011$$) en het getal 6 ($$00000110$$) zijn, dan geeft de
bitsgewijze `or` operator het patroon $$00001111$$, wat het getal 15
representeert.

```python
print( 11 | 6 )
```

Om de waarde van een enkele bit in een patroon op 1 te zetten (dit wordt
vaak genoemd het "zetten van een bit") kun je de bitsgewijze `or`
toepassen met een patroon dat bestaat uit alleen maar nullen, met
uitzondering van een enkele 1 op de plek waar je de bit wilt zetten. Een
gemakkelijke manier om een bitpatroon te maken met alleen de juiste bit
gezet, is te starten met het getal 1, en dan de shift-links operator te
gebruiken om dit ene bit zover naar links te schuiven als nodig is. Neem
een getal en zet de bit met index 7 (dus de achtste bit vanaf rechts
geteld) op 1.

### Bitsgewijze `not`

De bitsgewijze `not` operator (`\~`) wordt voor een bitpatroon
geplaatst, en produceert een nieuw bitpatroon dat alle bits van het
originele patroon "geflipt" heeft (dus iedere 0 wordt een 1, en iedere 1
wordt een 0). Bijvoorbeeld, als het originele patroon het getal 11
($$00001011$$) is, dan produceert de bitsgewijze `not` het patroon
$$11110100$$, wat het getal $$-12$$ is. Als je je afvraagt waarom het $$-12$$
is en niet $$-11$$: dat komt door het twee-complement systeem dat ik
hierboven heb uitgelegd. Maak je er maar niet druk over.

```python
print( ~11 )
```

Om een enkele bit in een patroon op 0 te zetten, kun je de bitsgewijze
`and` gebruiken met een patroon dat bestaat uit alleen maar enen, met
uitzondering van een 0 op de plek waar je de bit op 0 wilt zetten. Een
gemakkelijke manier om een dergelijk bitpatroon te maken, is te beginnen
met het getal 1, de shift-links operator te gebruiken om die 1 te
verschuiven naar de positie die je op 0 wilt zetten, en dan het patroon
te inverteren middels de bitsgewijze `not` operator. Neem een getal en
zet de bit met index 3 (de vierde bit van rechts) op 0.

### Bitsgewijze `xor`

De bitsgewijze `exclusieve or`, of "xor," operator (`^`) neemt twee
bitpatronen, en produceert een nieuw bitpatroon dat een 0 heeft op alle
posities waarbij de originele patronen dezelfde waarde hebben, en een 1
op alle posities waar de originele bitpatronen verschillend zijn.
Bijvoorbeeld, als de originele patronen het getal 11 ($$00001011$$) en het
getal 6 ($$00000110$$) zijn, dan geeft de bitsgewijze `xor` operator het
patroon $$00001101$$, wat het getal 13 is.

```python
print( 11 ^ 6 )
```

De bitsgewijze `xor` operator geeft een gemakkelijke manier om getallen
te versleutelen. Neem een bitpatroon en noem dat het "masker." Pas dat
masker toe op een getal via de `xor`. Dat geeft een nieuw getal, dat het
versleutelde getal is. Iemand die het masker niet kent, kan het
originele getal niet herleiden. Maar iemand die het masker wel kent, kan
het originele getal eenvoudigweg terugkrijgen door het masker opnieuw
toe te passen op het versleutelde getal. Probeer dit.

### Afhandelingsvolgorde van bitsgewijze operatoren

*Waarschuwing*: de afhandelingsvolgorde van bitsgewijze operatoren is
*niet* dat ze afgehandeld worden vóór de andere operatoren. Zorg ervoor
dat je haakjes gebruikt om de operatoren op de juiste volgorde toe te
passen als je bitsgewijze operatoren gebruikt in een berekening.
Bijvoorbeeld, je denkt misschien dat `1<<1 + 2<<1` hetzelfde is als
`1*2 + 2*2`, maar in werkelijkheid wordt het uitgevoerd als
`(1<<(1+2))<<1`, ofwel `1*8*2`.

```python
print( 1<<1 + 2<<1 )
print( (1<<1) + (2<<1) )
```
