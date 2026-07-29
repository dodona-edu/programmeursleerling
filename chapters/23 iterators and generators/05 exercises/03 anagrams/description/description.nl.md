Vraag de gebruiker om een
woord in te geven. Produceer alle anagrammen van dat woord. Als het
woord bepaalde letters dubbel bevat, is het acceptabel als bepaalde
anagrammen meerdere malen geproduceerd worden. Bijvoorbeeld, als het
woord `"gen"` is, produceer je `"eng"`, `"egn"`, `"gen"`, `"gne"`,
`"neg"`, en `"nge"` (volgorde maakt niet uit).

### Opgave

Schrijf een **generator**-functie `anagrammen` waaraan een woord
`woord` (`str`) moet doorgegeven worden. De generator moet alle
anagrammen van `woord` opleveren, als `str`-waarden. De volgorde
waarin de anagrammen opgeleverd worden maakt niet uit, en als `woord`
een letter meer dan één keer bevat, mag je bepaalde anagrammen meer
dan één keer opleveren; je hoeft deze duplicaten niet te filteren.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> sorted(anagrammen('gen'))
['egn', 'eng', 'gen', 'gne', 'neg', 'nge']

>>> sorted(set(anagrammen('raar')))
['aarr', 'arar', 'arra', 'raar', 'rara', 'rraa']
```
