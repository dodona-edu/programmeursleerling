HTML en XML zijn standaardformaten die gebruikt worden om informatie op
webpagina's te tonen. Ze bestaan uit leesbare tekst, waarin
formatteringsinstructies zijn opgenomen. Data analisten moeten
regelmatig data "schrapen" uit webpagina's. Je kunt daar reguliere
expressies voor gebruiken, maar als de pagina's redelijk fatsoenlijk
geformatteerd zijn, kun je de "Beautiful Soup" module gebruiken.

De Beautiful Soup module wordt in Python `bs4` genoemd (`bs3` kwam
ervoor, en er kunnen meer updates volgen). De module bevat de
`BeautifulSoup` class die je kunt gebruiken om HTML en XML bestanden te
laden. `bs4` wordt niet standaard door Python ondersteund; je moet het
apart installeren, wat een beetje gedoe geeft, tenzij je gebruik maak
van het `pip` programma dat wel standaard met Python 3 wordt
meegeleverd.

Een alternatief voor Beautiful Soup is de `lxml` module, maar de
eerstgenoemde is populairder.

Omdat dit soort modules apart installaties nodig hebben, ga ik ze niet
hier beschrijven. Ik wil alleen aangeven dat als je data uit webpagina's
wilt halen (en dat moet je inderdaad waarschijnlijk doen op een bepaald
moment), je beter eerst de standaard hulpmiddelen die beschikbaar zijn
kunt bestuderen voordat je je werpt op het ontwerpen van excentrieke
reguliere expressies.
