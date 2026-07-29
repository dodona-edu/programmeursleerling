Als vervolg op de vorige opgave,
schrijf je nu een decompressie programma voor de geproduceerde strings.

Hint: Je doet gewoon het omgekeerde van wat je in de vorige opgave deed:
bouw de half-byte-list opnieuw. Die list kun je dan gemakkelijk vertalen
naar de originele string.

### Opgave

Schrijf een functie `decomprimeer` waaraan een byte string (`bytes`) moet doorgegeven worden die geproduceerd werd door het compressieprogramma uit de vorige opgave. De functie moet de tekst (`str`) teruggeven die tot die byte string gecomprimeerd werd.

Let op de halve byte met waarde nul die eventueel achteraan de byte string toegevoegd werd om haar laatste byte te vervolledigen. Zo'n halve byte is opvulling, en niet het begin van een niet-geëncodeerd teken.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> decomprimeer(b'\x04\x81\xbb@,\xf0wI\xba\x02\x10')
'Hello, world!'
>>> decomprimeer(b'\x124Vx\x9a\xbc\xde\xf0')
'etaoinshrdlcum '
>>> decomprimeer(b'\x05\x10W\x04PR\x05@Y')
'QWERTY'
>>> decomprimeer(b'')
''
```
