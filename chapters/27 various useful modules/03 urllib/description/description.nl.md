De `urllib` module geeft je de mogelijkheid om webpagina's te benaderen
zoals je bestanden benadert. Er zijn twee modules die van belang zijn:
`urllib.request` bevat functies om informatie op het Internet te
benaderen, en `urllib.error` bevat definities van exceptions die
gegenereerd kunnen worden. Je kunt `urllib` ook gebruiken om te
communiceren met webpagina's; als je dat wilt doen, moet je de
`urllib.parse` module bestuderen. Ik geef hier alleen een eenvoudig
voorbeeld waarin de inhoud van een webpagina wordt gelezen.

```python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import exit

try:
    u = urlopen( "http://www.python.org" )
except HTTPError as e:
    print( "HTTP Error", e )
    sys.exit()
except URLError as e:
    print( "URL error", e )
    sys.exit()

for i in range( 5 ):
    tekst = u.readline()
    print( tekst )

u.close()
```

Merk op dat van `urllib` alleen `urlopen` geïmporteerd hoeft te worden.
Zodra je een webpagina hebt geopend, beschik je over een handle, waarop
je de reguliere methodes kunt gebruiken die zijn uitgelegd in hoofdstuk
17.
