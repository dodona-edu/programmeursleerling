Net als strings, zijn tuples onveranderbaar. Dat wil zeggen dat je geen
nieuwe waarde kunt toekennen aan een element van een tuple. Het
voorbeeld hieronder veroorzaakt een runtime error als je het uitvoert.

```python
t1 = ("appel", "banaan", "kers", "doerian")
t1[0] = "mango" # Runtime error
```
