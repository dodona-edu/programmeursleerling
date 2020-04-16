Een bitstring (`str`) is een patroon dat enkel bestaat uit enen (`1`) en nullen (`0`).

Schrijf een functie `bitmask` waaraan twee stringargumenten (`str`) moeten doorgegeven worden: een string $$s$$ en een bitstring $$m$$. De functie moet de versleuteling van $$s$$ (`str`) teruggeven die men bekomt via de bitsgewijze exclusieve or (xor) met $$m$$ als masker.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> bitmask('Hello, world!', '00101010')
'bOFFE\x06\n]EXFN\\x0b'
>>> bitmask('bOFFE\x06\\n]EXFN\x0b', '00101010')
'Hello, world!'
```
