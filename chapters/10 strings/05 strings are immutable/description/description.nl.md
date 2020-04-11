Een kerneigenschap van strings is dat ze onveranderbaar (Engels:
"immutable") zijn. Dit betekent dat strings niet kunnen wijzigen.
Bijvoorbeeld, je kunt niet een teken in een string wijzigen door er een
nieuwe waarde aan toe te kennen. Ter demonstratie: de volgende code
leidt tot een runtime error als je hem probeert uit te voeren:

```python
fruit = "aaldbei"
fruit[2] = "r"  # Runtime error!
print( fruit )
```

Als je een wijziging wilt maken in een string, moet je een nieuwe string
maken die de wijziging omvat; je kunt daarna de nieuwe string toekennen
aan de bestaande variabele als je wilt. Bijvoorbeeld:

```python
fruit = "aaldbei"
fruit = fruit[:2] + "r" + fruit[3:]
print( fruit )
```

De reden waarom strings onveranderbaar zijn, is te technisch om hier te
bespreken. Onthoud alleen dat als je een string wilt wijzigen, je geen
nieuwe waarde kunt toekennen aan een individueel teken uit de string. In
plaats daarvan moet je de variabele die de string bevat geheel
overschrijven.
