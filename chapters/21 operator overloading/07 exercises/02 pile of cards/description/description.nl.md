Gebruik de class `Kaart` van de
vorige opgave. Creëer ook een class `Trekstapel`. Een `Trekstapel` is
een sequentie van kaarten. De kaarten vormen een stapel met de laagste
index voor de bovenste kaart, en de hoogste index voor de onderste
kaart. Implementeer de `__len__()` en `__getitem__()` methodes. Creëer
een `voegtoe()` methode die een kaart toevoegt aan de stapel aan de
onderkant, en een `trek()` methode om een kaart aan de bovenkant van de
stapel te verwijderen en te retourneren. Test de class.

### Opgave

Definieer opnieuw de klasse `Kaart` van de vorige opgave (je oplossing wordt op zichzelf beoordeeld, en kan dus niets importeren uit een andere opgave). Een kaart (`Kaart`) wordt aangemaakt op basis van een kleur (`'Harten'`, `'Schoppen'`, `'Klaveren'` of `'Ruiten'`) en een waarde (`2` tot en met `10`, `'Boer'`, `'Vrouw'`, `'Heer'` of `'Aas'`), er moet een `AssertionError` met de boodschap `ongeldige kaart` opgeworpen worden als één van beide ongeldig is, `repr` leest als een Python expressie waarmee dezelfde kaart aangemaakt wordt, `str` beschrijft de kaart in de vorm `Aas van Harten`, en de vergelijkingsoperatoren vergelijken twee kaarten enkel op hun waarde.

Definieer ook een klasse `Trekstapel` waarmee een trekstapel van kaarten kan voorgesteld worden. Bij het aanmaken van een trekstapel (`Trekstapel`) mag één optioneel argument doorgegeven worden: een lijst (`list`) van kaarten (`Kaart`) die de stapel vormen, met de bovenste kaart van de stapel op index 0 en de onderste kaart op de laatste index. Als er geen argument doorgegeven wordt, dan moet een lege trekstapel aangemaakt worden.

Trekstapels (`Trekstapel`) moeten minstens de volgende bewerkingen ondersteunen:

- De ingebouwde functie `len` moet het aantal kaarten (`int`) op de stapel teruggeven.

- Indexering van een trekstapel (`stapel[i]`) moet de kaart (`Kaart`) op positie $$i$$ van de stapel teruggeven.

- Een methode `voegtoe` waaraan een kaart (`Kaart`) moet doorgegeven worden, die onderaan de stapel gelegd wordt. De methode geeft geen waarde terug.

- Een methode `trek` die de bovenste kaart van de stapel verwijdert en teruggeeft (`Kaart`). Als de stapel leeg is, dan moet de waarde `None` teruggegeven worden.

- Als een trekstapel doorgegeven wordt aan de ingebouwde functies `repr` of `str`, dan moet een string (`str`) teruggegeven worden die leest als een Python expressie waarmee dezelfde trekstapel aangemaakt wordt.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> stapel = Trekstapel([Kaart('Harten', 4), Kaart('Klaveren', 7), Kaart('Schoppen', 'Vrouw')])
>>> stapel
Trekstapel([Kaart('Harten', 4), Kaart('Klaveren', 7), Kaart('Schoppen', 'Vrouw')])
>>> len(stapel)
3
>>> stapel[0]
Kaart('Harten', 4)
>>> stapel[0] < stapel[2]
True
>>> stapel.voegtoe(Kaart('Ruiten', 'Aas'))
>>> len(stapel)
4
>>> stapel.trek()
Kaart('Harten', 4)
>>> stapel
Trekstapel([Kaart('Klaveren', 7), Kaart('Schoppen', 'Vrouw'), Kaart('Ruiten', 'Aas')])

>>> leeg = Trekstapel()
>>> len(leeg)
0
>>> leeg.trek()
>>> leeg.voegtoe(Kaart('Ruiten', 10))
>>> leeg
Trekstapel([Kaart('Ruiten', 10)])
```
