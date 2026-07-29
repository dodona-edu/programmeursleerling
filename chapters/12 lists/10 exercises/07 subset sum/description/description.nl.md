Het "subset som" probleem stelt de vraag of
een bepaalde verzameling van integers een deelverzameling van integers
bevat die, als ze worden opgeteld, nul als antwoord geven. Bijvoorbeeld,
als de verzameling is opgeslagen als een list, dan is het antwoord bij
de list `[1, 4, -3, -5, 7]` "ja," aangezien $1 + 4 - 5 = 0$. Echter,
voor de list `[1, 4, -3, 7]` is het antwoord "nee," aangezien er geen
deelverzameling van de integers is die optellen tot nul. Schrijf een
programma dat het subset som probleem oplost voor een list met integers.
Als er een oplossing is, druk die af; als er geen oplossing is, geef dat
dan aan.

Hint: Dit probleem pak je het beste aan met recursie. Als je hoofdstuk
10
hebt overgeslagen, kun je het beste ook deze opgave overslaan.

### Opgave

Schrijf een functie `subset_som` waaraan een lijst (`list`) van gehele getallen (`int`) moet doorgegeven worden. De functie moet een lijst (`list`) teruggeven met een deelverzameling van de gegeven getallen die optelt tot nul. Die deelverzameling moet minstens één getal bevatten, en mag geen enkel getal vaker gebruiken dan het in de gegeven lijst voorkomt. Als er geen dergelijke deelverzameling bestaat, dan moet de functie `None` teruggeven.

Er kan meer dan één deelverzameling zijn die optelt tot nul. In dat geval mag de functie om het even welke daarvan teruggeven.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> subset_som([1, 4, -3, -5, 7])
[1, 4, -5]
>>> subset_som([1, 4, -3, 7])
>>> subset_som([17, -4, -4, -4, -4, -1])
[17, -4, -4, -4, -4, -1]
```
