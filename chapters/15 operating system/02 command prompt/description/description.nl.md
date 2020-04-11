Als je werkt met een muisbestuurde "user interface" (UI), standaard bij
Windows en Mac OS, en ook vaak gebruikt bij Linux, ben je in
werkelijkheid aan het communiceren met een visuele representatie van het
systeem, of meer specifiek: het bestandssysteem. Programma's en
documenten zijn weergegeven middels "pictogrammen" (Engels: "icons"),
die een naam hebben. Ze zijn gegroepeerd in "folders," die in
werkelijkheid "directories" zijn van het bestandssysteem. Je kunt nieuwe
folders creëren, documenten verwijderen, programma's hernoemen,
beveiligingen wijzigen, etcetera. Al deze acties kun je ook uitvoeren
door direct commando's te typen, in een omgeving die vaak een "command
prompt" of "command shell" wordt genoemd.

Linux gebruikers zijn veelal bekend met de command shell, maar Windows
en Mac gebruikers zijn zich meestal niet bewust van het bestaan ervan.
Zowel Windows als Mac hebben een programma dat je toestaat om te werken
in de command shell. Bij Windows heet het de "command prompt" en is het
te vinden bij de "accessories" of "system tools" (of de Nederlandse
varianten daarvan). Bij Mac heet het de "Terminal." Als je dat programma
start, zie je zwart schermpje met een knipperende prompt. Hier kun je
commando's typen die het besturingssysteem dan uitvoert.

De commando's die je kunt geven zijn afhankelijk van je systeem. Dit
boek is niet bedoeld om je te leren hoe je het systeem moet gebruiken,
maar ik wil in ieder geval aangeven dat je Python programma's kunt
uitvoeren in de command shell door het volgende commando te geven:

```console?lang=bash&prompt=$
$ python <programmanaam>.py
```

Als Python op je systeem gevonden kan worden, en het programma staat in
de huidige directory (dat wil zeggen, de plaats in het bestandssysteem
van de computer waar je je op dat moment bevindt), of als je het
complete pad naar het programma hebt opgegeven, dan wordt het programma
uitgevoerd. Dit kan handig zijn als je een programma hebt geschreven dat
bestanden verwerkt, en je wilt een groot aantal bestanden verwerken als
een "batch." Wederom, dat gaat te diep voor dit boek, maar je kunt op
een punt in je carrière belanden waar dit extreem handig kan zijn.

De commando's die je kunt geven zijn zaken als "wijzig de huidige
directory," "maak een nieuwe directory," "verwijder een lege directory,"
"produceer een lijst van alle bestanden in de directory," "verwijder een
bestand," etcetera. Wederom, het is afhankelijk van het
besturingssysteem wat je geacht wordt te doen om deze zaken te
bewerkstelligen.

Zoek op je systeem op waar je de command shell kunt starten en voer het
programma uit. Op Windows, typ "dir" om de bestanden in de huidige
directory te zien. Op Mac en Linux doe je dit meestal met "ls." Nadat je
dit geprobeerd hebt, kun je de command shell weer sluiten.
