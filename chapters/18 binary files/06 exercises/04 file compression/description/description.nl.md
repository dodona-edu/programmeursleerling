Hoewel dit hoofdstuk over binaire
bestanden gaat, werden in de vorige twee opgaves geen binaire bestanden
gebruikt. Er valt gewoon niet veel te oefenen met binaire bestanden: de
problemen bij dit soort bestanden betreffen het behandelen van bytes, en
dat is wat de vorige twee opgaves deden. Maar om te completeren wat deze
twee opgaves begonnen, kun je nu een programma schrijven dat
tekstbestanden comprimeert en decomprimeert.

Schrijf een programma dat vraagt om een invoerbestand, dat moet bestaan,
en een uitvoerbestand, dat niet mag bestaan. Daarna vraagt het programma
of je wilt comprimeren of decomprimeren. Als je ervoor kiest om te
comprimeren, wordt het invoerbestand gecomprimeerd volgens de
bovengenoemde methode, en als uitvoerbestand weggeschreven. Als je
ervoor kiest om te decomprimeren, wordt het invoerbestand
gedecomprimeerd onder de aanname dat het eerder gecomprimeerd is middels
de bovengenoemde methode, en als uitvoerbestand weggeschreven. Dus je
zou het originele tekstbestand weer terug moeten kunnen krijgen door
eerst te comprimeren en dat te decomprimeren.

Je doet er goed aan eerst het hele bestand in het geheugen te lezen
voordat je gaat (de)comprimeren, zodat je niet in de problemen komt als
de byte string in een halve byte eindigt in plaats van in een hele byte
na compressie. Je doet er ook goed aan zowel het invoerbestand als het
uitvoerbestand als binaire bestanden te behandelen.
