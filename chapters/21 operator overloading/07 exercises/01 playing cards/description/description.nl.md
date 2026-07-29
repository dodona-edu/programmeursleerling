Een speelkaart heeft een kleur
(`"Harten", "Schoppen", "Klaveren", "Ruiten"`) en een waarde
(`2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Vrouw", "Heer", "Aas"`).
Implementeer een class `Kaart`. Zorg ervoor dat twee kaarten gelijk zijn
als ze een gelijke waarde hebben, en dat andere vergelijkingen de
volgorde van de waardes gebruiken (dus met 2 als laagste waarde en Aas
als hoogste waarde). Test de nieuwe class.

### Opgave

Definieer een klasse `Kaart` waarmee speelkaarten kunnen voorgesteld worden. Bij het aanmaken van een kaart (`Kaart`) moeten twee argumenten doorgegeven worden: *i*) de kleur (`str`) van de kaart, die één van de waarden `'Harten'`, `'Schoppen'`, `'Klaveren'` of `'Ruiten'` moet zijn, en *ii*) de waarde van de kaart, die één van de waarden `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` (`int`), `'Boer'`, `'Vrouw'`, `'Heer'` of `'Aas'` (`str`) moet zijn. Als een ongeldige kleur of een ongeldige waarde doorgegeven wordt, dan moet een `AssertionError` opgeworpen worden met de boodschap `ongeldige kaart`.

Kaarten (`Kaart`) moeten minstens de volgende bewerkingen ondersteunen:

- Als een kaart doorgegeven wordt aan de ingebouwde functie `repr`, dan moet een string (`str`) teruggegeven worden die leest als een Python expressie waarmee dezelfde kaart aangemaakt wordt. Als een kaart doorgegeven wordt aan de ingebouwde functie `str`, dan moet een string (`str`) teruggegeven worden die de kaart beschrijft in de vorm `Aas van Harten`.

- De vergelijkingsoperatoren `==`, `!=`, `<`, `<=`, `>` en `>=` moeten twee kaarten enkel op hun waarde vergelijken, volgens de volgorde waarin de waardes hierboven opgesomd worden (`2` is de laagste waarde en `'Aas'` de hoogste). De kleur speelt geen rol bij deze vergelijkingen, waardoor twee kaarten met dezelfde waarde gelijk zijn, ook al hebben ze een verschillende kleur.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> kaart_1 = Kaart('Harten', 'Aas')
>>> kaart_2 = Kaart('Schoppen', 'Heer')
>>> kaart_3 = Kaart('Klaveren', 'Heer')
>>> kaart_1
Kaart('Harten', 'Aas')
>>> print(kaart_2)
Heer van Schoppen
>>> str(kaart_3)
'Heer van Klaveren'
>>> kaart_1 == kaart_2
False
>>> kaart_2 == kaart_3
True
>>> kaart_1 > kaart_2
True
>>> kaart_2 >= kaart_3
True
>>> kaart_1 < kaart_3
False
>>> sorted([kaart_1, kaart_2, kaart_3])
[Kaart('Schoppen', 'Heer'), Kaart('Klaveren', 'Heer'), Kaart('Harten', 'Aas')]
>>> Kaart('Bomen', 7)
Traceback (most recent call last):
AssertionError: ongeldige kaart
```
