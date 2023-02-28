Een generator is een functie die het gedrag van een iterabel object
emuleert. Over het algemeen is het korter en gemakkelijker om een
generator te bouwen dan het is om een iterabele te bouwen. Diverse
standaardfuncties zijn als generator geïmplementeerd, bijvoorbeeld de
functie `range()`.

Generatoren zijn gebaseerd op het gereserveerde woord `yield`. Als
`__next__()` wordt aangeroepen voor een generator, wordt de functie
uitgevoerd totdat `yield` wordt aangetroffen, en dan wordt de waarde
geretourneerd die met de `yield` geassocieerd is. Daar aangekomen,
"wacht" de functie totdat `__next__()` opnieuw wordt aangeroepen, waarna
de functie verder gaat waar hij gebleven was totdat `yield` weer
gevonden wordt. `StopIteration` wordt automatisch gegenereerd wanneer de
functie eindigt.

Je hoeft niet expliciet `__next__()` en/of `__iter__()` te definiëren
voor een generator. Een generator bestaat bij gratie van het feit dat de
functie het gereserveerde woord `yield` bevat, en het geassocieerde
iterabele object wordt automatisch door Python gecreëerd, inclusief
correcte implementaties voor `__next__()` en `__iter__()`.

```python
def fibo( maxnum ):
    nr1 = 0
    nr2 = 1
    while nr2 <= maxnum:
        nr3 = nr1 + nr2
        nr1 = nr2
        nr2 = nr3
        yield nr1

fseq = fibo( 1000 )
for n in fseq:
    print( n, end=" " )
print()
for n in fseq:
    print( n, end=" " )
```

### Generator expressies

In hoofdstuk
13
introduceerde ik het concept "list comprehension." Omdat een list in een
iterator veranderd kan worden, en daarom in een generator, heeft Python
een gelijksoortig concept geïntroduceerd voor generatoren, en noemt dit
"generator expressies." De syntax van een generator expressie is gelijk
aan de syntax van een list comprehension, behalve dat er ronde in plaats
van vierkante haken omheen staan.

Bijvoorbeeld, de volgende generator expressie retourneert alle kwadraten
tot en met 100:

```python
seq = (x*x for x in range( 11 ))
for x in seq:
    print( x, end=" " )
```

Als je de twee buitenste haakjes in de generator expressie wijzigt in
vierkante haken, wordt de code uitgevoerd met `seq` als resultaat van
een list comprehension. Om hierover heel duidelijk te zijn: met list
comprehension wordt de hele list in één keer gegenereerd, terwijl met
een generator expressie de elementen pas gegenereerd worden wanneer ze
nodig zijn. Daarom is in principe een generator expressie te prefereren,
aangezien die minder geheugen nodig heeft.
