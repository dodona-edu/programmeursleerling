A bitstring (`str`) is pattern that only consists of zeroes (`0`) and ones (`0`).

Write a function `bitmask` that takes two string (`str`) arguments: a string $$s$$ (`str`) and a bitstring $$m$$. The function must return the string (`str`) obtained by encoding $$s$$ using the bitwise exclusive or (xor) with mask $$m$$.

### Example

```console?lang=python&prompt=>>>
>>> bitmask('Hello, world!', '00101010')
'bOFFE\x06\n]EXFN\\x0b'
>>> bitmask('bOFFE\x06\\n]EXFN\x0b', '00101010')
'Hello, world!'
```
