Stel je een nieuw data type voor. Dit nieuwe
data type noem ik de `inttuple`. Een `inttuple` is gedefinieerd als
zijnde ofwel een integer, ofwel een tuple die `inttuple`s als waardes
bevat. Je ziet een voorbeeld van een `inttuple` hieronder.

```console?lang=python&prompt=>>>
>>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
```

### Opgave

Schrijf een functie `afvlakken` waaraan een `inttuple` moet doorgegeven worden. De functie moet een `tuple` teruggeven die alle integer waardes bevat die in een `inttuple` zijn opgeslagen.

{:class="callout callout-info"}
> #### Tip
> Omdat de `inttuple` recursief is gedefinieerd, is een recursieve functie waarschijnlijk de beste aanpak. Als je hoofdstuk <a href="#ch:recursion" data-reference-type="ref" data-reference="ch:recursion">10</a> hebt overgeslagen, kun je waarschijnlijk deze opdracht beter ook overslaan. Als je hem wel maakt, dan kun je de `isinstance()` functie (uitgelegd in hoofdstuk <a href="#ch:functions" data-reference-type="ref" data-reference="ch:functions">9</a>) gebruiken om te bepalen of een element een integer of een tuple is.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> inttuple = (1, 2, (3, 4), 5, ((6, 7, 8, (9, 10), 11), 12, 13), ((14, 15, 16), (17, 18, 19, 20)))
>>> afvlakken(inttuple)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
```
