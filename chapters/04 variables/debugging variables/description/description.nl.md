Een veelvoorkomende oorzaak van functionele fouten in programma's is dat
variabelen blijken niet de waardes te bevatten waarvan je dacht dat ze
ze bevatten. Een goede manier om je code te “debuggen” (dat wil zeggen,
uit te vinden waar in je code fouten staan en die te verbeteren) is het
printen van variabele namen op geschikte plaatsen. Bijvoorbeeld, de
volgende code geeft een foutmelding als je hem uitvoert.

```python
nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
```

Misschien zie je wat het probleem is, maar stel dat je het niet ziet,
hoe vind je dan uit wat er mis is? Je ziet dat de fout ontdekt wordt op
regel 10, wat wil zeggen dat alles nog steeds werkte op regel 9. Als je
een extra regel code zet tussen regel 9 en 10, die de waarde afdrukt van
`nr1`, `nr2`, `nr3` and misschien ook `nr1 % nr2`, dan ontdek je
waarschijnlijk snel wat er misloopt. `print()` statements veranderen
niks aan de variabelen, dus je kunt ze veilig toevoegen. Een
fatsoenlijke manier om het probleem in deze code op te lossen (dus een
andere manier dan gewoon de laatste regel te verwijderen) zal ik in een
later hoofdstuk introduceren.

Voeg de extra regel toe aan de foute code.
