As a collary to the previous
exercise, write a decompression program for the produced strings.

Hint: Just do the opposite of what you did in the previous exercise:
rebuild the half-byte-list. That list is then easily converted back to
the original string.

### Assignment

Write a function `decompress` that takes a byte string (`bytes`) that was produced by the compression program from the previous exercise. The function must return the text (`str`) that was compressed into that byte string.

Watch out for the zero half-byte that may have been added at the end of the byte string to complete its last byte. Such a half-byte is padding, not the start of an unencoded character.

### Example

```console?lang=python&prompt=>>>
>>> decompress(b'\x04\x81\xbb@,\xf0wI\xba\x02\x10')
'Hello, world!'
>>> decompress(b'\x124Vx\x9a\xbc\xde\xf0')
'etaoinshrdlcum '
>>> decompress(b'\x05\x10W\x04PR\x05@Y')
'QWERTY'
>>> decompress(b'')
''
```
