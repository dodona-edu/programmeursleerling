Een tuple bestaat uit een aantal waardes die van elkaar gescheiden zijn
met komma's. Meestal worden tuples geschreven met haakjes eromheen, maar
de haakjes zijn niet noodzakelijk (behalve in omstandigheden waar anders
verwarring zou ontstaan). Bijvoorbeeld:

```python
t1 = ("appel", "mango")
print( type( t1 ) )
t2 = "banaan", "kers"
print( type( t2 ) )
```

Je kunt in een tuple verschillende data types mixen.

```python
t1 = ("appel", 3, 1.4)
t2 = ("appel", 3, 1.4, ("banaan", 5))
```

Je kunt de `len()` functie gebruiken om te bepalen hoeveel elementen een
tuple heeft.

```python
t1 = ("appel", "mango")
t2 = ("appel", 3, 1.4)
t3 = ("appel", 3, 1.4, ("banaan", 5))
print( len( t1 ) )
print( len( t2 ) )
print( len( t3 ) )
```

Merk op dat in dit voorbeeld de lengte van `t3` 4 is, en niet 5. Het
laatste element van `t3` is de tuple `("banaan", 5)`, wat telt als één
element.

Je kunt een `for` loop gebruiken om de elementen van een tuple te
doorlopen.

```python
t1 = ("appel", 3, 1.4, ("banaan", 5))
for element in t1:
    print( element )
```

Je kunt de `max()` en `min()` functies gebruiken om het maximum
respectievelijk het minimum te bepalen van een tuple die bestaat uit
getallen. Je kunt de elementen van een tuple met numerieke elementen bij
elkaar optellen middels de `sum()` functie.

```python
t1 = (327, 419, 101, 667, 925, 225)
print( max( t1 ) )
print( min( t1 ) )
print( sum( t1 ) )
```

Je kunt testen of een element onderdeel van een tuple is met behulp van
de `in` operator.

```python
t1 = ("appel", "banaan", "kers")
print( "banaan" in t1 )
print( "mango" in t1 )
```

### Tuple assignments

Je kunt een tuple creëren door een assignment van een aantal waardes
gescheiden door komma's aan een variabele. Haakjes zijn optioneel. Wat
als je een tuple wilt creëren met slechts één element?

```python
t1 = ("appel")
print( type( t1 ) )
```

Als je deze code uitvoert, zie je dat `t1` de class `str` heeft, dat wil
zeggen, `t1` is een string. Dat er haakjes omheen staan bij de
assignment maakt het niet tot een tuple. Python heeft een truukje om een
tuple met slechts één element te maken, namelijk door een komma te
plaatsen achter het ene element. Dit is niet erg intuïtief en ik zou het
zelfs wat zwak willen noemen, maar historisch was dit de oplossing die
een vroege versie van Python bevatte, en kennelijk heeft niemand iets
beters weten te verzinnen.

```python
t1 = ("appel",)
print( type( t1 ) )
print( len( t1 ) )
```

Python staat toe een tuple van variabelen links van de assignment
operator te plaatsen. Dit is een uitzondering op de regel dat slechts
één variabele links van de assignment operator staat. De waardes aan de
rechterkant worden één voor één naar de linkerkant gekopieerd, van links
naar rechts.

```python
t1, t2 = "appel", "banaan"
print( t1 )
print( t2 )
```

Je kunt haakjes om de waardes aan de rechterkant zetten, en je kunt ook
haakjes rond de variabelen aan de linkerkant zetten; dat maakt geen
verschil.

Als je meer variabelen aan de linkerkant zet dan waardes aan de
rechterkant, krijg je een runtime error. Hetzelfde geldt voor minder
(met als uitzondering dat je precies één variabele plaatst). Je kunt wel
tuples aan de rechterkant plaatsen door haakjes te gebruiken.

```python
t1, t2 = ("apple", "banaan"), "kers"
print( t1 )
print( t2 )
```

### Tuple indices

Net als bij strings, kun je individuele elementen van een tuple
benaderen via indices. Waar bij strings de individuele elementen tekens
zijn, zijn het bij tuples waardes. Bijvoorbeeld:

```python
t1 = ("appel", "banaan", "kers", "doerian")
print( t1[2] )
```

Je kunt zelfs sub-tuples maken, met dezelfde regels als je hebt voor
substrings (als je die niet meer weet, lees dan nog eens hoofdstuk
11).
Een sub-tuple is ook weer een tuple. Bijvoorbeeld:

```python
t1 = ("appel", "banaan", "kers", "doerian", "mango")
print( t1[1:4] )
```

Omdat tuples indices hebben, kun je als alternatief voor een `for` loop
om de elementen van de tuple te doorlopen, gebruik maken van de indices.

```python
t1 = ("appel", "banaan", "kers", "doerian", "mango")
i = 0
while i < len( t1 ):
    print( t1[i] )
    i += 1
```

Schrijf een `for` loop die alle elementen van een tuple toont, en die
ook hun indices toont.

### Tuple vergelijkingen

Je kunt twee tuples met elkaar vergelijken met behulp van de reguliere
vergelijkingsoperatoren. Deze operatoren vergelijken eerst de eerste
elementen van beide tuples. Als ze verschillend zijn, dan geeft de
vergelijking van die twee elementen op basis van de regels die voor hun
data types geldt, de gevraagde uitkomst. Als ze gelijk zijn, dan worden
de volgende elementen van beide tuples met elkaar vergeleken, etcetera.

```python
t1 = ( "appel", "banaan" )
t2 = ( "appel", "banaan" )
t3 = ( "appel", "kers" )
t4 = ( "appel", "banaan", "kers" )
print( t1 == t2 )
print( t1 < t3 )
print( t1 > t4 )
print( t3 > t4 )
```

### Tuple retourwaardes

In hoofdstuk
9
legde ik uit dat functies meerdere waardes kunnen retourneren. Als je
zoiets programmeert, dan komt het er in feite op neer dat de functie een
tuple retourneert. Om zulke retourwaardes af te handelen, doe je wat
hierboven beschreven is voor "tuple assignments.".
