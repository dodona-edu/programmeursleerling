Ask the user to enter a
word. Produce all anagrams of that word. If the word contains multiple
copies of a letter, it is acceptable if you produce certain anagrams
multiple times. For example, if the word is `"ape"`, you produce
`"aep"`, `"ape"`, `"eap"`, `"epa"`, `"pae"`, and `"pea"` (in any order).

### Assignment

Write a **generator** function `anagrams` that takes one argument
`word` (`str`). The generator must yield all anagrams of `word`, as
`str` values. The order in which the anagrams are yielded does not
matter, and if `word` contains a letter more than once, some anagrams
may be yielded more than once; there is no need to filter out these
duplicates.

### Example

```console?lang=python&prompt=>>>
>>> sorted(anagrams('ape'))
['aep', 'ape', 'eap', 'epa', 'pae', 'pea']

>>> sorted(set(anagrams('eve')))
['eev', 'eve', 'vee']
```
