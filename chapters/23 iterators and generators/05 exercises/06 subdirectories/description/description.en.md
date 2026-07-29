Write a program that
produces all possible sub-dictionaries from a dictionary, and stores
them in a list. For instance, if the dictionary is `\{"a":1,"b":2\}`,
the program produces `[\{\},\{"a":1\},\{"b":2\},\{"a":1,"b":2\}]` (the
ordering of the list does not matter). Again, use the `itertools`
module.

### Assignment

Write a function `sub_dictionaries` that takes one `dict` and returns
a `list` containing all its sub-dictionaries: every dictionary that can
be formed by keeping some subset of the key/value pairs of the given
dictionary. This includes the empty dictionary and the dictionary
itself. The order of the sub-dictionaries in the returned list does not
matter, and neither does the order of the key/value pairs within each
sub-dictionary.

### Example

```console?lang=python&prompt=>>>
>>> sub_dictionaries({"a": 1, "b": 2})
[{}, {'a': 1}, {'b': 2}, {'a': 1, 'b': 2}]

>>> sorted(sorted(sub.items()) for sub in sub_dictionaries({"x": 3, "y": 8}))
[[], [('x', 3)], [('x', 3), ('y', 8)], [('y', 8)]]
```
