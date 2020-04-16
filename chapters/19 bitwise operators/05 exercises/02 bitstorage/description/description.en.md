- Write a function `setbit` that takes three arguments: an integer $$n$$ (`int`, $$0 \leq n < 256$$), an integer $$i$$ (`int`, $$0 \leq i < 8$$) and a Boolean value $$b$$ (`bool`). The integer $$n$$ is used to store Boolean values: each bit either represents `True` (`1`) or `False` (`0`). The bits of $$n$$ are numbered as the convention indicates, with the rightmost bit having number zero, the bit next to that number 1, etcetera. If the Boolean value that is passed to the function is `True`, the function must the bit of $$n$$ at position $$i$$ to 1. If the Boolean value that is passed to the function is `False`, the function must the bit of $$n$$ at position $$i$$ to 0. The function must return the value that is obtained in this way.

- Write a function `getbit` that takes two arguments: an integer $$n$$ (`int`, $$0 \leq n < 256$$) and an integer $$i$$ (`int`, $$0 \leq i < 8$$). These arguments have the same meaning as with the function `setbit`. The function must return a Boolean value (`bool`) that indicates if the bit of $$n$$ at position $$i$$ is 1.

- Write a function `bitstring` that takes an integer $$n$$ (`int`, $$0 \leq n < 256$$). The function must return the representation of $$n$$ as a bitstring (`str`).

### Example

```console?lang=python&prompt=>>>
>>> store = setbit(0, 0, True)
>>> store
1
>>> getbit(store, 0)
True
>>> bitstring(store)
'00000001'
>>> store = setbit(store, 1, True)
>>> store
3
>>> getbit(store, 1)
True
>>> bitstring(store)
'00000011'
>>> store = setbit(store, 2, False)
>>> store
3
>>> getbit(store, 2)
False
>>> bitstring(store)
'00000011'
>>> store = setbit(store, 3, True)
>>> store
11
>>> getbit(store, 3)
True
>>> bitstring(store)
'00001011'
>>> store = setbit(store, 4, False)
>>> store
11
>>> getbit(store, 4)
False
>>> bitstring(store)
'00001011'
>>> store = setbit(store, 5, True)
>>> store
43
>>> getbit(store, 5)
True
>>> bitstring(store)
'00101011'
>>> store = setbit(store, 1, False)
>>> store
41
>>> getbit(store, 1)
False
>>> bitstring(store)
'00101001'
```
