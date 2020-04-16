- Schrijf een functie `setbit` waaraan drie argumenten moeten doorgegeven worden: een integer $$n$$ (`int`, $$0 \leq n < 256$$), een integer $$i$$ (`int`, $$0 \leq i < 8$$) en een Booleaanse waarde $$b$$ (`bool`). De integer $$n$$ wordt gebruikt om Booleaanse waarden op te slaan: iedere bit stelt ofwel `True` (`1`) of `False` (`0`) voor. De bits van $$n$$ zijn op de
conventionele manier genummerd, met index 0 voor de meest rechter bit. Als de boolean die is meegegeven `True` is, dan moet de functie de bit van $$n$$ op positie $$i$$ op 1 zetten. Als de boolean die is meegegeven `False` is, dan moet de functie de bit van $$n$$ op positie $$i$$ op 0 zetten. De functie moet de waarde teruggeven die op die manier bekomen wordt.

- Schrijf een functie `getbit` waaraan twee argumenten moeten doorgegeven worden: een integer $$n$$ (`int`, $$0 \leq n < 256$$) en een integer $$i$$ (`int`, $$0 \leq i < 8$$). Deze argumenten hebben dezelfde betekenis als bij de functie `setbit`. De functie moet een Booleaanse waarde (`bool`) teruggeven, die aangeeft of de bit van $$n$$ op positie $$i$$ een 1 is.

- Schrijf een functie `bitstring` waaraan een integer $$n$$ (`int`, $$0 \leq n < 256$$) moet doorgegeven worden. De functie moet de voorstelling van $$n$$ als bitstring (`str`) teruggeven.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> opslag = setbit(0, 0, True)
>>> opslag
1
>>> getbit(opslag, 0)
True
>>> bitstring(opslag)
'00000001'
>>> opslag = setbit(opslag, 1, True)
>>> opslag
3
>>> getbit(opslag, 1)
True
>>> bitstring(opslag)
'00000011'
>>> opslag = setbit(opslag, 2, False)
>>> opslag
3
>>> getbit(opslag, 2)
False
>>> bitstring(opslag)
'00000011'
>>> opslag = setbit(opslag, 3, True)
>>> opslag
11
>>> getbit(opslag, 3)
True
>>> bitstring(opslag)
'00001011'
>>> opslag = setbit(opslag, 4, False)
>>> opslag
11
>>> getbit(opslag, 4)
False
>>> bitstring(opslag)
'00001011'
>>> opslag = setbit(opslag, 5, True)
>>> opslag
43
>>> getbit(opslag, 5)
True
>>> bitstring(opslag)
'00101011'
>>> opslag = setbit(opslag, 1, False)
>>> opslag
41
>>> getbit(opslag, 1)
False
>>> bitstring(opslag)
'00101001'
```
