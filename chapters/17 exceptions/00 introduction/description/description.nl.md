Soms treden runtime errors op niet omdat je een programmeerfout hebt
gemaakt, maar omdat er een probleem optreedt dat je niet kon voorzien
toen je het programma schreef. Dit is buitengewoon relevant als je met
bestanden werkt: bijvoorbeeld, als je een bestand verwerkt dat op een
USB-stick staat, en de gebruiker verwijdert de USB-stick tijdens de
verwerking, krijg je uiteraard een fout die je niet echt zou kunnen
voorzien in je code. Iedere runtime error genereert in de code een
zogenaamde "exception" ("uitzondering") die je kunt "afvangen." Het
afvangen van een exception betekent dat je in je programma code opneemt
die ervoor zorgt dat de opgetreden fout zoveel mogelijk netjes wordt
afgehandeld, in plaats van je programma abrupt af te breken.
