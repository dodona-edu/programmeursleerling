Het "subset som" probleem
stelt de vraag of een bepaalde verzameling van integers een
deelverzameling van integers bevat die, als ze worden opgeteld, nul als
antwoord geven. Bijvoorbeeld, als de verzameling is opgeslagen als een
list, dan is het antwoord bij de list `[1, 4, -3, -5, 7]` "ja,"
aangezien $1 + 4 - 5 = 0$. Echter, voor de list `[1, 4, -3, 7]` is het
antwoord "nee," aangezien er geen deelverzameling van de integers is die
optellen tot nul. Schrijf een programma dat het subset som probleem
oplost voor een list met integers. Als er een oplossing is, druk die af;
als er geen oplossing is, geef dat dan aan.

Dit is een herhaling van één van de opgaves uit hoofdstuk
13
(Lists). In dat hoofdstuk zei ik dat je deze opgave het beste recursief
kunt aanpakken. Echter, door de `itertools` module te gebruiken, kun je
hem nu oplossen zonder recursie (ik vermoed dat recursie nog steeds
plaatsvindt in de `itertools` module, maar jij hoeft je er niet druk om
te maken).
