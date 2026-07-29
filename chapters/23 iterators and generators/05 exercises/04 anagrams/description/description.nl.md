Doe de voorgaande opgave
nogmaals, maar zorg er nu voor dat alle anagrammen uniek zijn, zelfs als
het woord dubbele letters bevat. Bijvoorbeeld, als het woord `"aap"` is,
produceer je `"aap"`, `"apa"`, en `"paa"`.

### Opgave

Schrijf een **generatorfunctie** `unieke_anagrammen` waaraan een woord `woord` (`str`) wordt doorgegeven. De functie moet elk uniek anagram van `woord` exact één keer opleveren, als een string (`str`). De volgorde waarin de anagrammen opgeleverd worden maakt niet uit.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> sorted(unieke_anagrammen("aap"))
['aap', 'apa', 'paa']

>>> sorted(unieke_anagrammen("kat"))
['akt', 'atk', 'kat', 'kta', 'tak', 'tka']
```
